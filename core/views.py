from random import randint
from django.db.models import Min, Max
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BackgroundImage, MusicTrack, Quote
from .serializers import BackgroundImageSerializer, MusicTrackSerializer, QuoteSerializer

def pick_random(model):
    qs = model.objects.filter(is_active=True)
    ids = qs.aggregate(min_id=Min("id"), max_id=Max("id"))
    if not ids["min_id"]:
        return None
    for _ in range(6):
        pk = randint(ids["min_id"], ids["max_id"])
        obj = qs.filter(id__gte=pk).order_by("id").first()
        if obj:
            return obj
    return qs.order_by("id").first()  # 兜底

class RandomBackgroundImage(APIView):
    def get(self, request):
        obj = pick_random(BackgroundImage)
        if not obj:
            return Response({"detail": "no image"}, status=404)

        data = BackgroundImageSerializer(obj).data
        # 拼接完整 URL
        if 'image' in data and data['image']:
            data['image'] = request.build_absolute_uri(data['image'])

        return Response(data)


class RandomMusicTrack(APIView):
    def get(self, request):
        obj = pick_random(MusicTrack)
        if not obj:
            return Response({"detail": "no music"}, status=404)

        data = MusicTrackSerializer(obj).data
        if 'audio' in data and data['audio']:
            data['audio'] = request.build_absolute_uri(data['audio'])

        return Response(data)

class RandomQuote(APIView):
    def get(self, request):
        # 可支持按语言过滤：/api/random/quote?lang=zh
        lang = request.GET.get("lang")
        model = Quote
        if lang:
            orig_pick = pick_random
            def pick_with_lang(m):
                from django.db.models import Min, Max
                qs = m.objects.filter(is_active=True, language=lang)
                ids = qs.aggregate(min_id=Min("id"), max_id=Max("id"))
                if not ids["min_id"]:
                    return None
                from random import randint
                for _ in range(6):
                    pk = randint(ids["min_id"], ids["max_id"])
                    obj = qs.filter(id__gte=pk).order_by("id").first()
                    if obj: return obj
                return qs.order_by("id").first()
            obj = pick_with_lang(model)
        else:
            obj = pick_random(model)

        if not obj:
            return Response({"detail": "no quote"}, status=404)
        return Response(QuoteSerializer(obj).data)

