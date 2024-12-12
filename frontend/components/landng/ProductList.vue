<template>
 <div class="w-full mt-[10vw] md:mt-[5.5vw] px-[3.75vw] md:px-[10.8vw]" ref="elementRef">
    <div class="flex select-none items-center text-[#791A4D] justify-between">
        <div :class="['text-[5vw] md:text-[1.6vw] transition-all duration-200 ease-out',currentLanguage==='ar' ? 'cairo' : currentLanguage==='ir' ? 'vazir': 'montserrat', animationStart ? 'rtl:translate-x-0 ltr:translate-x-0 opacity-100':'ltr:translate-x-[-5vw] opacity-0 rtl:translate-x-[5vw]']">{{ t('latestProducts') }}</div>
        <NuxtLink to="/products" :class="['text-[3.5vw] transition-all duration-200 ease-out md:text-[1vw] cursor-pointer',currentLanguage==='ar' ? 'cairo' : currentLanguage==='ir' ? 'vazir' : 'montserrat', animationStart ? ' rtl:translate-x-0 opacity-100 ltr:translate-x-0' : ' opacity-0 ltr:translate-x-[5vw] rtl:translate-x-[-5vw]' ]">{{ t('more') }}</NuxtLink>
    </div>
    <div :class="['w-full mt-[7vw] md:mt-[4.1vw] items-center flex justify-between delay-200 transition-all duration-300 ease-out', !animationStart ? ' translate-y-[5vw] opacity-0' : ' opacity-100 translate-y-0']">
        <svg @click="previousSlide" class="w-[15vw] ltr:rotate-0 rtl:rotate-180 h-[15vw] md:h-[4.8vw] md:w-[4.8vw] cursor-pointer" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18.7148 28.0078L34.6523 12.0703C35.7539 10.9688 37.5352 10.9688 38.625 12.0703L41.2734 14.7187C42.375 15.8203 42.375 17.6016 41.2734 18.6914L29.9883 30L41.2852 41.2969C42.3867 42.3984 42.3867 44.1797 41.2852 45.2695L38.6367 47.9297C37.5352 49.0312 35.7539 49.0312 34.6641 47.9297L18.7266 31.9922C17.6133 30.8906 17.6133 29.1094 18.7148 28.0078Z" fill="#791A4D"/>
</svg>
<div class="flex-grow  flex h-[90vw] w-[70vw] md:h-[27.1vw] overflow-hidden">
    <div class="flex h-full whitespace-nowrap transition-all duration-200" :style="sliderPosition">
        <div v-for="(product,index) in products" @click="openProduct(product.slug)" :key="index" class="w-full h-full px-[2vw] md:px-[1vw]">
            <div  class="flex-grow  select-none p-[4vw] md:p-[2.4vw] h-[90vw] flex flex-col w-[60vw] md:w-[20.8vw] md:h-[27.1vw] rounded-[3vw] border-[1px] cursor-pointer">
    <div class="w-full h-[31.55vw] md:h-[13vw]">
        <SkeletonLoading :class="['w-full rounded-[3vw] md:h-[13vw] h-[31.55vw]', imageLoaded[index] ? 'opacity-0' : 'opacity-100']"/>
        <div class="w-full h-[31.55vw] md:h-[13vw] inline-block relative md:-translate-y-[13vw] -translate-y-[31.55vw]">
            <NuxtImg @load="loadIndex(index)" :class="['w-full duration-200 transition-all h-full',imageLoaded[index] ? 'opacity-100' : 'opacity-0']" :src="product.image_url" alt="" />
        </div>
    </div>
    <div :class="['text-center md:text-[1.1vw] md:mt-[1vw] text-[4vw] mt-[4vw] text-[#791A4D]',currentLanguage==='ar' ? 'cairo': currentLanguage==='ir' ? 'vazir' : 'montserrat']">{{ currentLanguage==='ar' ? product.title_arabic : currentLanguage==='ir' ? product.title_persian : product.title }}</div>
    <div :class="['text-center md:text-[0.9vw] md:mt-[2.2vw] whitespace-normal mt-[6vw] text-[3.5vw] text-[#694956]', currentLanguage==='ar' ? 'cairo': currentLanguage==='ir' ?'vazir' : 'montserrat']">{{ currentLanguage==='ar' ? product.caption_arabic : currentLanguage==='ir' ? product.caption_persian : product.caption }}</div>
</div>
        </div>
    </div>
    
</div>

<svg @click="nextSlide" class="w-[15vw] ltr:rotate-180 rtl:rotate-0 h-[15vw] md:h-[4.8vw] md:w-[4.8vw] cursor-pointer" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18.7148 28.0078L34.6523 12.0703C35.7539 10.9688 37.5352 10.9688 38.625 12.0703L41.2734 14.7187C42.375 15.8203 42.375 17.6016 41.2734 18.6914L29.9883 30L41.2852 41.2969C42.3867 42.3984 42.3867 44.1797 41.2852 45.2695L38.6367 47.9297C37.5352 49.0312 35.7539 49.0312 34.6641 47.9297L18.7266 31.9922C17.6133 30.8906 17.6133 29.1094 18.7148 28.0078Z" fill="#791A4D"/>
</svg>

    </div>
 </div>
</template>
<script>
import SkeletonLoading from '../global/SkeletonLoading.vue';
export default {
    setup() {
      const { t, locale } = useI18n();
      const currentLanguage = computed(() => locale.value);
      const animationStart = ref(false);
    const observer = ref(null);
    const elementRef = ref(null); 
    const animateSection = () => {
        animationStart.value = true; 
        };
    const handleIntersect = (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateSection(); 

          observer.value.unobserve(entry.target);
        }
      });
    };
    onMounted(() => {
      observer.value = new IntersectionObserver(handleIntersect, {
        threshold: 0.6,
      });

      if (elementRef.value) {
        observer.value.observe(elementRef.value);
      }
    });

    onBeforeUnmount(() => {
      if (observer.value) {
        observer.value.disconnect(); 
      }
    });
      return {t, locale, currentLanguage, elementRef,animationStart}
   },
   data(){
      return {
        currentSlide :4,
        imageLoaded :[],
        windowWidth: window.innerWidth,
      }
   },
   components:{
    SkeletonLoading,
   },
  props: {
    products: {
      type: Array,
      required: true,
      default: () => [],
      validator: (items) => items.every(item => 
      typeof item.id === 'int' && 
        typeof item.image_url === 'string' &&
        typeof item.title === 'string' &&
        typeof item.title_arabic === 'string' &&
        typeof item.title_persian === 'string' && 
        typeof item.caption === 'string' &&
        typeof item.caption_arabic === 'string' && 
        typeof item.caption_persian === 'string' && 
        typeof item.slug ==='string'
      )
    }
  },
  computed:{
    screenWidth() {
      return this.windowWidth;
    },
    sliderPosition(){
        let dir = this.currentLanguage === 'en' ? 1 : 1
        let distance = this.windowWidth > 768 ? 68.35 : 64
        return 'transform:translateX(' + this.currentSlide *  dir * distance + 'vw);'
    }
  },
  methods:{
    openProduct(productId){
      console.log(productId)
            this.$router.push(`/productDetail/${productId}`);
        },
    updateWidth() {
      this.windowWidth = window.innerWidth;
      if(this.windowWidth<768){
       this.currentSlide = 4;
   }else{
    this.currentSlide = 1;
   }
    },
    nextSlide(){
      let maxSlideIndex = this.windowWidth > 768 ? 2 : this.products.length -1;
          if(this.currentSlide < maxSlideIndex){
            this.currentSlide++;
          }
    },
    previousSlide(){
          if(this.currentSlide>0){
            this.currentSlide--;
          }
    },
    loadIndex(index){
          this.imageLoaded[index] = true;
   }
  },
  mounted(){
   window.addEventListener('resize', this.updateWidth);
   this.updateWidth();
   
    for(let a =0; a< this.products.length;a++){
            this.imageLoaded.push(false)
    }
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
</style>