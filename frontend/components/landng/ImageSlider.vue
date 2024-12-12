<template>
   <div class="w-full relative select-none inline-block flex-col items-end px-[3.75vw] md:px-[7.7vw] md:mt-[4vw] mt-[10vw] h-[75vw] md:h-[41.6vw] overflow-hidden rounded-[3vw]">
   <div class=" block w-full overflow-hidden h-full rounded-[3vw]">
  <div class="flex transition-all duration-500 h-full ease-in-out" :style="sliderPosition">
   <div v-for="(slide, index) in sliderData" :key="index" class=" shrink-0 w-full h-full">
      <div class="h-full">
         <SkeletonLoading class="h-full  absolute  rounded-[3vw]">
    </SkeletonLoading>
   <div class=" inline-block relative overflow-hidden md:-translate-y-[41.6vw] w-full -translate-y-[75vw]">
      <NuxtImg loading="lazy" @load="loadIndex(index)" :class="{'h-[75vw] md:h-[41.6vw] object-cover transition-all w-full duration-200':true,'opacity-0' : !imageLoaded[index],'image-animate' : currentSlide === index && imageLoaded[index],'image-normal': currentSlide !==index,'opacity-100' : imageLoaded[index]}" :src="slide.image_url"/>
      <div class="h-full w-full absolute top-0 left-0 flex flex-col items-center bg-black/50">
         <div :class="['px-[2.5vw] md:px-[1.6vw]  text-[5.1vw] md:w-[44.6vw] md:mt-[18vw] md:pt-0 md:text-[1.6vw] select-none text-center pt-[6vw] text-white',currentLanguage === 'ar' ? 'cairo': (currentLanguage==='ir' ? 'vazir' : 'montserrat')]">
            {{ currentLanguage === 'ar' ? slide.text_arabic : (currentLanguage==='ir' ? slide.text_persian : slide.text) }}
         </div>
         <NuxtLink :to="slide.navigate_to" v-if="slide.has_button" class="flex mt-[6vw] md:mt-[2.5vw] md:px-[1.6vw] md:py-[0.7vw] transition-all duration-150 hover:bg-[#49112f] justify-center py-[2vw] px-[6vw] bg-[#791A4D] cursor-pointer select-none rounded-full items-center">
           <div  :class="['text-[3.25vw] md:text-[1.6vw] h-full text-white',currentLanguage ==='ar' ?'cairo' : (currentLanguage==='ir' ? 'vazir' : 'montserrat')]">
            {{ currentLanguage === 'ar' ? slide.button_text_arabic : (currentLanguage==='ir' ? slide.button_text_persian : slide.button_text) }}
           </div>
         </NuxtLink>
      </div>
   </div>

      </div>
    </div>
  </div>
   </div>
    
    <div class="absolute py-[3vw]  bottom-0 left-0 md:pb-[3.5vw] md:pt-[0.7vw]  px-[8vw] md:px-[24.3vw] w-full">
      <div class="w-full md:m-auto bg-[#D5C2C7] mb-[2.5vw] md:mb-[0.7vw] h-[1px] rounded-full"></div>
      <div class="flex justify-between items-center w-full">
         <div class="flex">
         <div :class="leftButtonClass" @click="previousSlide">
            <svg class="ltr:rotate-0 rtl:rotate-180 w-[5.75vw] h-[5vw] md:h-[1.4vw] md:w-[1.4vw]" viewBox="0 0 18 16" fill="none" xmlns="http://www.w3.org/2000/svg">
               <path d="M17.7109 8.5C17.7109 8.85156 17.4375 9.125 17.125 9.125H2.90625L8.17969 14.9844C8.41406 15.2188 8.41406 15.6094 8.14062 15.8438C8.02344 15.9609 7.86719 16 7.75 16C7.55469 16 7.39844 15.9609 7.28125 15.8047L1.03125 8.92969C0.796875 8.69531 0.796875 8.34375 1.03125 8.10938L7.28125 1.23438C7.51562 0.960938 7.90625 0.960938 8.14062 1.19531C8.41406 1.42969 8.41406 1.82031 8.17969 2.05469L2.90625 7.875H17.125C17.4375 7.875 17.7109 8.1875 17.7109 8.5Z" fill="white"/>
            </svg>
         </div>
         <div :class="rightButtonClass" @click="nextSlide">
            <svg class=" rtl:rotate-0 ltr:rotate-180 w-[5.75vw] h-[5vw] md:h-[1.4vw] md:w-[1.4vw]"  viewBox="0 0 18 16" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M17.7109 8.5C17.7109 8.85156 17.4375 9.125 17.125 9.125H2.90625L8.17969 14.9844C8.41406 15.2188 8.41406 15.6094 8.14062 15.8438C8.02344 15.9609 7.86719 16 7.75 16C7.55469 16 7.39844 15.9609 7.28125 15.8047L1.03125 8.92969C0.796875 8.69531 0.796875 8.34375 1.03125 8.10938L7.28125 1.23438C7.51562 0.960938 7.90625 0.960938 8.14062 1.19531C8.41406 1.42969 8.41406 1.82031 8.17969 2.05469L2.90625 7.875H17.125C17.4375 7.875 17.7109 8.1875 17.7109 8.5Z" fill="white"/>
            </svg>
         </div>
      </div>
      <div :class="['flex select-none  h-full justify-center items-center text-[4vw] md:text-[1vw] text-white ', currentLanguage === 'ar' ? 'cairo': (currentLanguage==='ir' ? 'vazir' : 'montserrat')]">
         <div>{{ currentSlideText + 1 }}</div>
         <div class="mx-[1vw] md:mx-[0.4vw]">{{ t('from') }}</div>
         <div>{{ sliderData.length }}</div>
      </div>
      </div>
    </div>
   </div>
</template>
<script>
import SkeletonLoading from '../global/SkeletonLoading.vue';
import { useI18n } from 'vue-i18n';

export default{
   components:{
      SkeletonLoading,
   },
   setup() {
      const { t, locale } = useI18n();
      const currentLanguage = computed(() => locale.value);
      return {t, locale,currentLanguage}
   },
   props:{
      sliderData: {
      type: Array,
      required: true,
      default: () => [],
      validator: (items) => items.every(item => 
        typeof item.text === 'string' &&
        typeof item.textAr === 'string' &&
        typeof item.imageUrl === 'string' &&
        typeof item.hasButton === 'boolean' &&
        typeof item.navigateTo === 'string' &&
        typeof item.buttonText === 'string' &&
        typeof item.buttonTextAr === 'string' && 
        typeof item.buttonTextIr === 'string' && 
        typeof item.textIr === 'string'
      )
    }
},
data(){
   return {
      currentSlide:0,
      imageLoaded:[],
      windowWidth: window.innerWidth,
      slidingDirection:'next',
      slidingDelay:10000,
   }
},
methods:{
   nextSlide(){
         if(this.currentSlide < this.sliderData.length-1){
         this.currentSlide++;
      }
      if(this.currentSlide === this.sliderData.length-1){
         this.slidingDirection = 'prev'
      }
   },
   updateWidth() {
      this.windowWidth = window.innerWidth;
    },
   previousSlide(){
         if(this.currentSlide>0){
         this.currentSlide--;
      }
      if(this.currentSlide ===0){
         this.slidingDirection = 'next'
      }
   
   },
   loadIndex(index){
          this.imageLoaded[index] = true;
   },
   automaticSlide(){
         setTimeout(()=>{
             this.slidingDirection === 'next' ? this.nextSlide() : this.previousSlide()
             this.automaticSlide()
         },this.slidingDelay)
   }
},
computed:{
   screenWidth() {
      return this.windowWidth;
    },
   currentSlideText(){
      return this.currentSlide
   },
   rightButtonClass(){
      return ['transition-all mx-[1.5vw] md:mx-[0.4vw] md:h-[2.8vw] md:w-[2.8vw] duration-200 cursor-pointer w-[10vw] h-[10vw] rounded-full flex justify-center items-center ' , this.currentSlide< this.sliderData.length-1  ? 'bg-[#791A4D]' : 'bg-[rgba(29, 27, 32, 0.12)]' ]
   },
   leftButtonClass(){
      return [ 'transition-all mx-[1.5vw] md:mx-[0.4vw] md:h-[2.8vw] md:w-[2.8vw] duration-200 cursor-pointer w-[10vw] h-[10vw] rounded-full flex justify-center items-center ' , this.currentSlide>0 ? 'bg-[#791A4D]' : 'bg-[rgba(29, 27, 32, 0.12)]']
   },
   sliderPosition(){
     let dir = this.currentLanguage === 'en' ? 1 : 1
      return 'transform:translateX('+ dir * this.currentSlide * 100 + '%);'
   }
},
mounted(){
   window.addEventListener('resize', this.updateWidth);
   this.updateWidth();
    for(let a =0; a< this.sliderData.length;a++){
            this.imageLoaded.push(false)
    }
    this.automaticSlide()
}
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@200..1000&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');


.cairo {
  font-family: "Cairo", sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
  font-variation-settings: "slnt" 0;
}
.montserrat{
  font-family: "Montserrat", sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
}
.image-normal{
   animation: scaleDown 0.01s linear 0.5s forwards;

}
.image-animate{
   animation: scaleUp 10s linear  forwards;
}
@keyframes scaleDown{
   from{
      transform: scale(1.5);
   }
   to{
      transform: scale(1);
   }
}
@keyframes scaleUp {
    from {
      transform: scale(1);
    }
    to {
      transform: scale(1.5);
    }
  }
</style>