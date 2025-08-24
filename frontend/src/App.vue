<template>
  <div
    class="relative w-full h-screen flex flex-col items-center justify-between"
    :style="{ backgroundImage: `url(${background?.image})`, backgroundSize: 'cover', backgroundPosition: 'center' }"
  >
    <!-- 灰色遮罩层 -->
    <div class="absolute inset-0 bg-black bg-opacity-25"></div>

    <!-- 顶部教言 -->
    <div class="relative z-10 mt-20 text-center px-6">
      <h1 class="text-4xl font-bold text-white drop-shadow-lg mb-6">
        -365颗钻石-
      </h1>
      <p class="text-2xl text-white drop-shadow-lg leading-relaxed">
        “{{ quote?.text }}”
      </p>
      <p class="text-base text-gray-200 drop-shadow-lg mt-4">
        —— {{ quote?.author }}
      </p>
    </div>

    <!-- 播放器部分 -->
    <div class="relative z-10 mb-24 flex flex-col items-center">
      <audio ref="audioRef" class="hidden" :src="music?.audio"></audio>
      <button
        @click="togglePlay"
        class="w-20 h-20 bg-black bg-opacity-60 rounded-full flex items-center justify-center text-white shadow-2xl active:scale-90 transition"
      >
        <!-- 使用 SVG 图标 -->
        <svg v-if="!isPlaying" xmlns="http://www.w3.org/2000/svg" class="w-10 h-10" viewBox="0 0 24 24" fill="currentColor">
          <path d="M8 5v14l11-7z"/>
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-10 h-10" viewBox="0 0 24 24" fill="currentColor">
          <path d="M6 19h4V5H6zm8-14v14h4V5h-4z"/>
        </svg>
      </button>
      <p class="text-white text-sm mt-3 drop-shadow-lg">{{ music?.title }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const API_BASE = "http://127.0.0.1:8000"; // 后端地址

const background = ref(null);
const music = ref(null);
const quote = ref(null);
const audioRef = ref(null);
const isPlaying = ref(false);

async function fetchRandom(api) {
  const res = await fetch(`/api/random/${api}`);
  if (!res.ok) return null;
  return res.json();
}

async function initPage() {
  const bg = await fetchRandom("image");
  const mu = await fetchRandom("music");
  const qt = await fetchRandom("quote?lang=zh");

  if (bg) bg.image = API_BASE + bg.image;
  if (mu) mu.audio = API_BASE + mu.audio;

  background.value = bg;
  music.value = mu;
  quote.value = qt;
}

function togglePlay() {
  if (!audioRef.value) return;
  if (isPlaying.value) {
    audioRef.value.pause();
    isPlaying.value = false;
  } else {
    audioRef.value.play();
    isPlaying.value = true;
  }
}

onMounted(initPage);
</script>

<style>
h1, p {
  text-shadow: 2px 2px 6px #000; /* 增强文字可读性 */
}
</style>

