<template>
  <div class="w-full mt-[10vw] md:mt-[5.5vw] md:px-[10.8vw]  px-[3.75vw] relative">
    <video       :style="{ backgroundColor: isLoaded ? 'transparent' : 'black' }"
    :src="videoUrl"  ref="video" @loadedmetadata="onLoadedMetadata" @timeupdate="onTimeUpdate" preload="none"
      controlslist="nodownload" class="w-full aspect-video rounded-[3vw] md:rounded-[0.8vw]">
      <source class="rounded-[3vw] md:rounded-[0.8vw]" :src="videoUrl" type="video/mp4">
    </video>

    <div
      class="controls relative h-[17vw] md:h-[5.68vw] translate-y-[-10vw] md:-translate-y-[5vw] rounded-b-[3vw] md:rounded-b-[0.8vw] bottom-0 w-full bg-[#791A4D] px-[4vw] md:px-[3.8vw] py-[1.38vw]">
      <!-- Progress Bar -->
      <input type="range" class="w-full appearance-none" min="0" max="100" step="1" v-model="progress" dir="ltr" @input="seek" />

      <div class="flex items-center justify-between ltr:flex-row rtl:flex-row-reverse w-full mt-[1vw]">
        <!-- Time Display -->
        <span class="text-[3.5vw] md:text-[1vw] text-white  font-mono montserrat">{{ formattedTime }}</span>
        <div class="flex items-center justify-center ">
          <svg @click="setToEnd"
            class="w-[6vw] mx-[1vw] ltr:rotate-0 rtl:rotate-180 h-[6vw] md:w-[1.38vw] md:h-[1.38vw] cursor-pointer"
            viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M19.7891 5C20.4141 5 21 5.54688 21 6.28906V18.75C21 19.4922 20.4141 20 19.7891 20C19.5156 20 19.2422 19.9219 19.0469 19.7656L13.0703 14.8438C12.8359 14.6484 12.7969 14.2578 12.9922 13.9844C13.2266 13.7109 13.6172 13.6719 13.8906 13.9062L19.75 18.7891V6.25L13.8906 11.1328C13.6172 11.3672 13.2266 11.3281 12.9922 11.0547C12.7969 10.7812 12.8359 10.3906 13.0703 10.1953L19.0469 5.27344C19.2422 5.11719 19.5156 5 19.7891 5ZM9.78906 5C10.1797 5 10.9609 5.35156 11 6.28906V18.75C11 19.6875 10.1797 20 9.78906 20C9.51562 20 9.24219 19.9219 9.04688 19.7266L1.42969 13.5156C1.15625 13.2812 1 12.8906 1 12.5C1 12.1484 1.15625 11.7578 1.42969 11.5234L9.04688 5.27344C9.24219 5.11719 9.51562 5 9.78906 5ZM9.75 18.7891V6.25L2.25 12.5L9.75 18.7891Z"
              fill="#FDF8F8" />
          </svg>
          <svg style="margin-left: 1vw !important;margin-right: 1vw;" v-if="!isPlaying" @click="togglePlayPause"
            class="w-[6vw] fill-white mx-[5vw] md:w-[1.38vw] md:h-[1.38vw] h-[6vw] cursor-pointer"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 384 512">
            <path
              d="M73 39c-14.8-9.1-33.4-9.4-48.5-.9S0 62.6 0 80L0 432c0 17.4 9.4 33.4 24.5 41.9s33.7 8.1 48.5-.9L361 297c14.3-8.7 23-24.2 23-41s-8.7-32.2-23-41L73 39z" />
          </svg>
          <svg v-else @click="togglePlayPause"
            class="w-[6vw] fill-white h-[6vw] md:w-[1.38vw] mx-[1vw] md:h-[1.38vw] cursor-pointer"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 320 512">
            <path
              d="M48 64C21.5 64 0 85.5 0 112L0 400c0 26.5 21.5 48 48 48l32 0c26.5 0 48-21.5 48-48l0-288c0-26.5-21.5-48-48-48L48 64zm192 0c-26.5 0-48 21.5-48 48l0 288c0 26.5 21.5 48 48 48l32 0c26.5 0 48-21.5 48-48l0-288c0-26.5-21.5-48-48-48l-32 0z" />
          </svg><svg @click="setToStart"
            class="w-[6vw] md:w-[1.38vw] md:h-[1.38vw] mx-[1vw] ltr:rotate-0 rtl:rotate-180 h-[6vw] fill-white cursor-pointer"
            viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M8.07031 11.1328L2.25 6.25V18.7891L8.07031 13.9062C8.34375 13.6719 8.73438 13.7109 8.96875 13.9844C9.16406 14.2578 9.125 14.6484 8.89062 14.8438L2.91406 19.7656C2.71875 19.9219 2.44531 20 2.17188 20C1.54688 20 1 19.4922 1 18.75V6.28906C1 5.54688 1.54688 5 2.17188 5C2.44531 5 2.71875 5.11719 2.91406 5.27344L8.89062 10.1953C9.125 10.3906 9.16406 10.7812 8.96875 11.0547C8.73438 11.3281 8.34375 11.3672 8.07031 11.1328ZM20.5312 11.5234C20.8047 11.7578 21 12.1484 21 12.5C21 12.8906 20.8047 13.2812 20.5312 13.5547L12.9141 19.7656C12.7188 19.9219 12.4453 20 12.1719 20C11.7812 20 11 19.6875 11 18.75V6.28906C11 5.35156 11.7812 5 12.1719 5C12.4453 5 12.7188 5.11719 12.9141 5.3125L20.5312 11.5234ZM12.25 18.7891L19.7109 12.5L12.25 6.25V18.7891Z"
              class=" fill-white" />
          </svg>

        </div>

        <div class="flex justify-center items-center  space-x-[2vw]">
          <svg @click="toggleMute" class="w-[6vw] md:w-[1.38vw] md:h-[1.38vw]  h-[6vw] cursor-pointer"
            viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M13.2578 3.86719C13.6875 4.0625 14 4.53125 14 5V20C14 20.5078 13.6875 20.9375 13.2578 21.1719C13.0625 21.25 12.9062 21.25 12.75 21.25C12.4375 21.25 12.125 21.1719 11.8906 20.8594L6.61719 16.1719H3.375C2.32031 16.1719 1.5 15.3516 1.5 14.3359V10.625C1.5 9.60938 2.32031 8.75 3.375 8.75H6.61719L11.8906 4.10156C12.125 3.86719 12.4375 3.75 12.75 3.75C12.9062 3.75 13.0625 3.78906 13.2578 3.86719ZM12.7109 20L12.6719 5.03906L7.08594 10H3.375C3.02344 10 2.75 10.2734 2.75 10.625V14.375C2.75 14.6875 3.02344 15 3.375 15H7.08594L12.7109 20ZM19.4297 6.36719C21.5 7.77344 22.75 10.0391 22.75 12.5C22.75 14.9609 21.5 17.2656 19.4297 18.6719C19.3125 18.75 19.1953 18.75 19.0781 18.75C18.8828 18.75 18.6875 18.6719 18.5703 18.4766C18.375 18.2031 18.4531 17.8125 18.7266 17.6172C20.4453 16.4844 21.5 14.5703 21.5 12.5C21.5 10.4688 20.4453 8.55469 18.7266 7.42188C18.4531 7.22656 18.375 6.83594 18.5703 6.5625C18.7656 6.25 19.1562 6.17188 19.4297 6.36719ZM17.3594 9.49219C18.375 10.1953 19 11.3281 19 12.5C19 13.7109 18.375 14.8438 17.3594 15.5469C17.2422 15.625 17.125 15.625 17.0078 15.625C16.8125 15.625 16.6172 15.5469 16.5 15.3516C16.3047 15.0781 16.3828 14.6875 16.6562 14.4922C17.3203 14.0625 17.75 13.3203 17.75 12.5C17.75 11.7188 17.3203 10.9766 16.6562 10.5469C16.3828 10.3516 16.3047 9.96094 16.5 9.6875C16.6953 9.375 17.0859 9.29688 17.3594 9.49219Z"
              fill="#FDF8F8" />
          </svg>
          <input type="range" min="0" max="1" step="0.1" v-model="volume" @input="changeVolume"
            class="w-[11.25vw] mt-[1vw] md:mt-0 appearance-none bg-white h-1 rounded" style="width: 12vw;" />
          <svg @click="toggleFullscreen" class="w-[6vw] md:w-[1.38vw] md:h-[1.38vw] h-[6vw] cursor-pointer"
            viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M7.875 3.75C8.1875 3.75 8.5 4.0625 8.5 4.375C8.5 4.72656 8.1875 5 7.875 5H3.5V9.375C3.5 9.72656 3.1875 10 2.875 10C2.52344 10 2.25 9.72656 2.25 9.375V4.375C2.25 4.0625 2.52344 3.75 2.875 3.75H7.875ZM7.875 20C8.1875 20 8.5 20.3125 8.5 20.625C8.5 20.9766 8.1875 21.25 7.875 21.25H2.875C2.52344 21.25 2.25 20.9766 2.25 20.625V15.625C2.25 15.3125 2.52344 15 2.875 15C3.1875 15 3.5 15.3125 3.5 15.625V20H7.875ZM19.125 15C19.4375 15 19.75 15.3125 19.75 15.625V20.625C19.75 20.9766 19.4375 21.25 19.125 21.25H14.125C13.7734 21.25 13.5 20.9766 13.5 20.625C13.5 20.3125 13.7734 20 14.125 20H18.5V15.625C18.5 15.3125 18.7734 15 19.125 15ZM19.125 3.75C19.4375 3.75 19.75 4.0625 19.75 4.375V9.375C19.75 9.72656 19.4375 10 19.125 10C18.7734 10 18.5 9.72656 18.5 9.375V5H14.125C13.7734 5 13.5 4.72656 13.5 4.375C13.5 4.0625 13.7734 3.75 14.125 3.75H19.125Z"
              fill="#FDF8F8" />
          </svg>

        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
     // replace with your video URL
      isPlaying: false,
      isLoaded: false,
      progress: 0,
      currentTime: 0,
    };
  },
  props:{
      videoUrl:{
        type:String,
        Required : true
      }
  },
  mounted(){
    this.setToStart()
  },
  computed: {
    formattedTime() {
      const minutes = Math.floor(this.currentTime / 60);
      const seconds = Math.floor(this.currentTime % 60);
      return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    },
  },
  methods: {
    onLoadedMetadata() {
      this.isLoaded = true;
    },
    togglePlayPause() {
      const video = this.$refs.video;
      if (this.isPlaying) {
        video.pause();
      } else {
        video.play();
      }
      this.isPlaying = !this.isPlaying;
    },
    setToStart() {
      const video = this.$refs.video;
      video.currentTime = 0;
      this.currentTime = 0;
    },
    setToEnd() {
      const video = this.$refs.video;
      video.currentTime = video.duration;
      this.currentTime = video.duration;
    },
    seek() {
      const video = this.$refs.video;
      video.currentTime = (this.progress / 100) * video.duration;
      this.currentTime = video.currentTime;
    },
    onTimeUpdate() {
      const video = this.$refs.video;
    if (video.duration > 0) {
      this.progress = (video.currentTime / video.duration) * 100;
    }
    },
    toggleFullscreen() {
    const videoContainer = this.$refs.video

    if (!document.fullscreenElement && !document.webkitFullscreenElement && !document.mozFullScreenElement && !document.msFullscreenElement) {
      // Enter fullscreen
      if (videoContainer.requestFullscreen) {
        videoContainer.requestFullscreen();
      } else if (videoContainer.webkitRequestFullscreen) { // Safari
        videoContainer.webkitRequestFullscreen();
      } else if (videoContainer.mozRequestFullScreen) { // Firefox
        videoContainer.mozRequestFullScreen();
      } else if (videoContainer.msRequestFullscreen) { // IE/Edge
        videoContainer.msRequestFullscreen();
      }
    } else {
      // Exit fullscreen
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if (document.webkitExitFullscreen) { // Safari
        document.webkitExitFullscreen();
      } else if (document.mozCancelFullScreen) { // Firefox
        document.mozCancelFullScreen();
      } else if (document.msExitFullscreen) { // IE/Edge
        document.msExitFullscreen();
      }
    }
  }
  },
};
</script>
<style scoped>
.controls {
  @apply p-2;
}

button img {
  @apply w-5 h-5;
}

input[type="range"] {
  @apply appearance-none w-full bg-gray-300 h-1 rounded;
}

/* Custom Thumb Styling */
input[type="range"]::-webkit-slider-thumb {
  @apply appearance-none bg-white w-[3vw] h-[3vw] md:w-[1.25vw] md:h-[1.25vw] rounded-full cursor-pointer;
}

input[type="range"]::-moz-range-progress {
  background-color: #ffffff;
  /* Filled section color */
}
</style>
