<template>
    <div class="w-full px-[3.75vw] select-none" ref="elementRef">
        <h1 :class="['text-[1.6vw] w-full mt-[5.5vw] px-[4vw] md:block hidden text-[#791A4D] text-center rtl:md:text-right ltr:md:text-left transition-all duration-200 ease-out',animationStart ? 'ltr:translate-x-0 rtl:translate-x-0 opacity-100':'rtl:translate-x-[10vw] ltr:-translate-x-[10vw] opacity-0', currentLanguage==='en' ? 'montserrat' : 'cairo']">{{ currentLanguage === 'ar' ? sloganAr : (currentLanguage==='ir' ? sloganIr : slogan) }}</h1>
        <div class="w-full flex flex-col md:flex-row justify-center">
            <img src="../../public/assets/images/truck.svg" :class="['w-full h-full md:w-[31.25vw] md:h-[31.25vw] transition-all duration-700 ease-out ', animationStart ? 'rtl:translate-x-0 ltr:translate-x-0 opacity-100' : 'rtl:translate-x-[15vw] ltr:translate-x-[-15vw] opacity-0']" alt="">
            <div :class="['text-[5.5vw] md:hidden  w-full text-[#791A4D] text-center transition-all duration-200 delay-200', currentLanguage==='en' ? 'montserrat' : (currentLanguage==='ir' ? 'vazir' : 'cairo'), animationStart ? 'ltr:translate-x-0 rtl:translate-x-0 opacity-100' : 'opacity-0 ltr:translate-x-[-20vw] rtl:translate-x-[20vw]']">{{ currentLanguage === 'ar' ? sloganAr : (currentLanguage==='ir' ? sloganIr : slogan) }}</div>
     <div class="block md:flex md:justify-center md:items-center">
        <div class="flex flex-col md:grid md:grid-cols-2 md:ltr:pr-[7.7vw] md:rtl:pl-[7.7vw] gap-[3.9vw] md:h-[16.1vw]">
            <div :class="['px-[15.8vw] md:px-[2.2vw] md:h-[4.4vw] h-[15vw] flex rtl:flex-row-reverse rtl:justify-start ltr:justify-end ltr:flex-row justify-end transition-all duration-300 delay-[350ms] md:delay-150', animationStart ? 'rtl:translate-x-0 ltr:translate-x-0 opacity-100' : 'ltr:translate-x-[-7vw] rtl:translate-x-[7vw] opacity-0']">
                <div class="flex ltr:justify-end  rtl:justify-start md:justify-center md:items-center items-center">
                    <div :class="['text-[3.7vw] mx-[4vw] w-full ltr:text-right rtl:text-left md:text-[1.1vw]',currentLanguage ==='en' ? 'montserrat' : (currentLanguage==='ir' ? 'vazir' : 'cairo')]">{{ t('quality') }}</div>
                    <svg class="w-[10vw] h-[15vw]" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M26.5 28.0469C25.4062 28.6719 23.7656 28.0469 22.5156 28.3594C21.3438 28.6719 20.25 30 19 30C17.6719 30 16.5781 28.6719 15.4062 28.3594C14.1562 28.0469 12.5156 28.6719 11.4219 28.0469C10.3281 27.4219 10.0938 25.7031 9.23438 24.7656C8.29688 23.9062 6.57812 23.5938 5.95312 22.5781C5.32812 21.4844 5.95312 19.8438 5.64062 18.5938C5.32812 17.4219 4 16.3281 4 15C4 13.75 5.32812 12.6562 5.64062 11.4844C5.95312 10.2344 5.32812 8.59375 5.95312 7.5C6.57812 6.40625 8.29688 6.17188 9.23438 5.3125C10.0938 4.375 10.4062 2.65625 11.4219 2.03125C12.5156 1.40625 14.1562 2.03125 15.4062 1.71875C16.5781 1.40625 17.6719 0 19 0C20.25 0 21.3438 1.40625 22.4375 1.71875C23.6875 2.03125 25.3281 1.40625 26.4219 2.03125C27.5156 2.65625 27.75 4.375 28.6875 5.3125C29.5469 6.17188 31.2656 6.40625 31.8906 7.5C32.5156 8.59375 31.8906 10.2344 32.2031 11.4844C32.5156 12.6562 33.9219 13.75 33.9219 15C33.9219 16.3281 32.5938 17.4219 32.2812 18.5938C31.9688 19.8438 32.5938 21.4844 31.9688 22.5781C31.3438 23.6719 29.625 23.9062 28.6875 24.7656C27.8281 25.7031 27.5156 27.4219 26.5 28.0469ZM18.9219 27.5C19.625 27.1875 20.5625 26.3281 21.8906 25.9375C23.2188 25.625 24.4688 25.8594 25.1719 25.8594C25.5625 25.2344 26.0312 23.9844 26.9688 23.0469C27.9062 22.1094 29.1562 21.6406 29.7812 21.25C29.7812 20.4688 29.5469 19.2188 29.8594 17.9688C30.25 16.6406 31.1094 15.7031 31.4219 15.0781C31.1094 14.375 30.25 13.4375 29.8594 12.1094C29.5469 10.7812 29.7812 9.53125 29.7812 8.82812C29.1562 8.4375 27.9062 7.96875 26.9688 7.03125C26.0312 6.09375 25.5625 4.84375 25.1719 4.21875C24.4688 4.21875 23.2188 4.45312 21.8906 4.14062C20.5625 3.75 19.625 2.89062 18.9219 2.57812C18.2969 2.89062 17.3594 3.75 16.0312 4.14062C14.7031 4.45312 13.4531 4.21875 12.75 4.21875C12.3594 4.84375 11.8906 6.09375 10.9531 7.03125C10.0156 7.96875 8.76562 8.4375 8.14062 8.82812C8.14062 9.53125 8.375 10.7812 8.0625 12.1094C7.67188 13.4375 6.8125 14.375 6.5 15.0781C6.8125 15.7031 7.67188 16.6406 8.0625 17.9688C8.375 19.2969 8.14062 20.5469 8.14062 21.25C8.6875 21.6406 9.9375 22.1094 10.875 23.0469C11.8125 23.9844 12.2812 25.2344 12.6719 25.7812C13.375 25.8594 14.625 25.625 15.9531 25.9375C17.2812 26.3281 18.2969 27.1875 18.9219 27.5ZM25.7969 15C25.7969 18.8281 22.5938 21.875 18.9219 21.875C15.1719 21.875 12.125 18.8281 12.125 15C12.125 11.25 15.25 8.125 19 8.125C22.6719 8.125 25.7969 11.25 25.7969 15ZM19 19.375C21.3438 19.375 23.2969 17.4219 23.2969 15C23.2969 12.6562 21.2656 10.625 18.9219 10.625C16.5781 10.625 14.625 12.6562 14.625 15C14.625 17.4219 16.5781 19.375 19 19.375ZM31.8906 28.9844L33.7656 33.75C34.1562 34.6094 34 35.7031 33.375 36.4062C32.75 37.1875 31.7344 37.5 30.7969 37.3438L29.0781 36.9531L28.2969 38.5938C27.8281 39.4531 26.9688 40 25.9531 40C24.7812 40 23.9219 39.375 23.5312 38.3594L21.5781 33.5938C21.2656 32.9688 21.5781 32.2656 22.2031 31.9531C22.9062 31.7188 23.6094 32.0312 23.8438 32.6562L25.7969 37.4219L27.75 34.1406L31.4219 34.6875L29.5469 29.8438C29.3125 29.2188 29.625 28.5156 30.25 28.2812C30.875 27.9688 31.6562 28.2812 31.8906 28.9844ZM15.7188 31.9531C16.3438 32.2656 16.6562 32.9688 16.3438 33.5938L14.3906 38.3594C14 39.375 13.1406 40 12.0469 40C10.9531 40 10.0938 39.4531 9.625 38.5938L8.84375 36.9531L7.125 37.3438C6.1875 37.5 5.17188 37.1875 4.54688 36.4062C3.92188 35.7031 3.76562 34.6094 4.15625 33.75L6.03125 28.9844C6.26562 28.2812 7.04688 27.9688 7.67188 28.2812C8.29688 28.5156 8.60938 29.2188 8.375 29.8438L6.5 34.6875L10.1719 34.1406L12.125 37.4219L14.0781 32.6562C14.3125 32.0312 15.0156 31.7188 15.7188 31.9531Z" fill="#791A4D"/>
</svg>
                </div>
            </div>
            <div :class="['px-[15.8vw] md:px-[2.2vw] md:h-[4.4vw] h-[15vw] flex rtl:flex-row-reverse rtl:justify-start ltr:justify-end ltr:flex-row justify-end transition-all duration-300 delay-500 md:delay-300', animationStart ? 'rtl:translate-x-0 ltr:translate-x-0 opacity-100' : 'ltr:translate-x-[-7vw] rtl:translate-x-[7vw] opacity-0']">
                <div class="flex ltr:justify-end  rtl:justify-start md:justify-center md:items-center items-center">
<div :class="['text-[3.7vw] mx-[4vw] w-full ltr:text-right rtl:text-left md:text-[1.1vw]',currentLanguage ==='en' ? 'montserrat' : (currentLanguage==='ir' ? 'vazir' : 'cairo')]">{{ t('packaging') }}</div>
<svg class="h-[8vw] w-[10vw]" viewBox="0 0 51 40" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M44.75 17.5C45.375 17.5 46 18.125 46 18.75V29.5312C46 31.25 44.8281 32.7344 43.1094 33.2031L27.4844 37.3438C26.9375 37.5 26.3906 37.5 25.9219 37.5C25.4531 37.5 24.9062 37.5 24.3594 37.3438L8.73438 33.2031C7.09375 32.7344 6 31.25 6 29.5312V18.75C6 18.125 6.54688 17.5 7.25 17.5C7.875 17.5 8.5 18.125 8.5 18.75V29.5312C8.5 30.0781 8.8125 30.625 9.35938 30.7031L24.75 34.7656V17.5C24.75 16.7969 25.2969 16.25 26 16.25C26.625 16.25 27.25 16.7969 27.25 17.5V34.8438L42.5625 30.7031C43.1094 30.5469 43.5 30.0781 43.5 29.4531V18.75C43.5 18.0469 44.0469 17.5 44.75 17.5ZM50.8438 12.0312C51 12.3438 51 12.7344 50.8438 13.125C50.6875 13.4375 50.375 13.6719 49.9844 13.75L33.7344 17.5C33.6562 17.5 33.5781 17.5 33.5 17.5C33.1094 17.5 32.7188 17.3438 32.4844 16.9531L26 8.35938L19.4375 17.0312C19.2031 17.3438 18.8125 17.5 18.5 17.5C18.3438 17.5 18.2656 17.5 18.1875 17.5L1.9375 13.75C1.54688 13.6719 1.23438 13.4375 1.07812 13.125C0.921875 12.7344 0.921875 12.4219 1.07812 12.0312L4.82812 3.28125C5.0625 2.8125 5.53125 2.5 6.07812 2.57812L26 5L45.8438 2.57812C46.3906 2.5 46.8594 2.8125 47.0938 3.28125L50.8438 12.0312ZM17.9531 14.9219L23.6562 7.26562L6.70312 5.15625L3.96875 11.6406L17.9531 14.9219ZM33.9688 14.9219L47.9531 11.6406L45.2188 5.15625L28.2656 7.26562L33.9688 14.9219Z" fill="#791A4D"/>
</svg>
                </div>
            </div>
            <div :class="['px-[15.8vw] md:px-[2.2vw] md:h-[4.4vw] h-[15vw] flex rtl:flex-row-reverse rtl:justify-start ltr:justify-end ltr:flex-row justify-end transition-all duration-300 delay-[650ms] md:delay-[450ms]', animationStart ? 'rtl:translate-x-0 ltr:translate-x-0 opacity-100' : 'ltr:translate-x-[-7vw] rtl:translate-x-[7vw] opacity-0']">
                <div class="flex ltr:justify-end  rtl:justify-start md:justify-center md:items-center items-center">
                    <div :class="['text-[3.7vw] mx-[4vw] w-full ltr:text-right rtl:text-left md:text-[1.1vw]',currentLanguage ==='en' ? 'montserrat' : (currentLanguage==='ir' ? 'vazir' : 'cairo')]">{{ t('price') }}</div>
                    <svg class="w-[10vw] h-[10vw]" viewBox="0 0 41 40" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M40.4219 20C40.4219 22.8125 38.9375 25.3906 36.5938 26.7188C37.2969 29.375 36.5156 32.1875 34.5625 34.1406C32.5312 36.25 29.7188 36.875 27.1406 36.1719C25.8125 38.5156 23.2344 40 20.4219 40C17.6875 40 15.1094 38.5156 13.7812 36.1719C11.2812 36.875 8.39062 36.25 6.28125 34.1406C4.32812 32.1875 3.625 29.375 4.32812 26.7188C1.98438 25.3906 0.421875 22.8125 0.421875 20C0.421875 17.2656 1.98438 14.6875 4.32812 13.3594C3.625 10.7031 4.40625 7.89062 6.28125 5.85938C8.23438 3.90625 11.125 3.20312 13.7812 3.90625C15.1094 1.5625 17.6875 0 20.4219 0C23.2344 0 25.8125 1.5625 27.1406 3.90625C29.7969 3.20312 32.6094 3.90625 34.5625 5.85938C36.5156 7.89062 37.2969 10.7031 36.5938 13.3594C38.9375 14.6875 40.4219 17.2656 40.4219 20ZM33.3125 25.3906C34.0938 25.0781 38 24.1406 38 20C38 16.0156 34.3281 15.0781 33.3125 14.6875C33.7031 13.9844 35.7344 10.5469 32.8438 7.65625C30.0312 4.84375 26.75 6.71875 25.8125 7.1875C25.5 6.40625 24.5625 2.5 20.5 2.5C16.5156 2.5 15.5 6.17188 15.1094 7.1875C14.4062 6.79688 10.9688 4.76562 8.07812 7.65625C5.26562 10.4688 7.14062 13.75 7.60938 14.6875C6.82812 15 3 15.9375 3 20C3 23.9844 6.67188 25 7.60938 25.3906C7.21875 26.0938 5.1875 29.5312 8.07812 32.4219C10.3438 34.6875 12.6094 34.0625 15.1094 32.8906C15.4219 33.6719 16.3594 37.5 20.5 37.5C24.4844 37.5 25.4219 33.8281 25.8125 32.8906C28.3125 34.0625 30.5781 34.6875 32.8438 32.4219C35.6562 29.6094 33.7812 26.3281 33.3125 25.3906ZM20.8125 18.8281C23.1562 19.4531 26.6719 20.3906 26.0469 24.0625C25.6562 25.9375 24.0156 27.1875 21.75 27.5V28.75C21.75 29.4531 21.125 30 20.5 30C19.7969 30 19.25 29.4531 19.25 28.75V27.4219C18.5469 27.3438 18 27.1875 15.6562 26.4062C15.0312 26.25 14.6406 25.4688 14.875 24.8438C15.1094 24.2188 15.8125 23.8281 16.5156 24.0625C18.4688 24.7656 18.9375 24.8438 19.4844 24.9219C21.3594 25.2344 23.3125 24.9219 23.5469 23.5938C23.7812 22.5 23.0781 22.0312 20.1094 21.25L19.5625 21.0938C17.8438 20.625 14.25 19.6094 14.875 16.0156C15.2656 14.1406 16.9062 12.8906 19.25 12.5781V11.25C19.25 10.625 19.7969 10 20.5 10C21.125 10 21.75 10.625 21.75 11.25V12.6562C22.375 12.7344 23.1562 12.9688 24.1719 13.2812C24.7969 13.5156 25.1875 14.2188 24.9531 14.8438C24.7188 15.4688 24.0156 15.8594 23.3906 15.625C22.5312 15.3906 21.9062 15.2344 21.3594 15.1562C19.5625 14.8438 17.6094 15.1562 17.375 16.4844C17.2188 17.4219 17.5312 17.8906 20.1875 18.6719L20.8125 18.8281Z" fill="#791A4D"/>
</svg>
                </div>
            </div>
            <div :class="['px-[15.8vw] md:px-[2.2vw] md:h-[4.4vw] h-[15vw] flex rtl:flex-row-reverse rtl:justify-start ltr:justify-end ltr:flex-row justify-end transition-all duration-300 delay-[800ms] md:delay-[600ms]', animationStart ? 'rtl:translate-x-0 ltr:translate-x-0 opacity-100' : 'ltr:translate-x-[-7vw] rtl:translate-x-[7vw] opacity-0']">
                <div class="flex ltr:justify-end  rtl:justify-start md:justify-center md:items-center items-center">
                    <div :class="['text-[3.7vw] mx-[4vw] w-full ltr:text-right rtl:text-left md:text-[1.1vw]',currentLanguage ==='en' ? 'montserrat' : (currentLanguage==='ir' ? 'vazir' : 'cairo')]">{{ t('smallTruckText') }}</div>
                    <svg class="h-[8vw] w-[10vw]" viewBox="0 0 50 40" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M48.75 30C49.375 30 50 30.625 50 31.25C50 31.9531 49.375 32.5 48.75 32.5H45C45 36.6406 41.5625 40 37.5 40C33.3594 40 30 36.6406 30 32.5H20C20 36.6406 16.5625 40 12.5 40C8.35938 40 5 36.6406 5 32.5C2.1875 32.5 0 30.3125 0 27.5V5C0 2.26562 2.1875 0 5 0H27.5C30.2344 0 32.5 2.26562 32.5 5V7.5H37.5781C38.6719 7.5 39.6875 8.04688 40.3906 8.82812L45.9375 15.3125C46.9531 16.4844 47.5 17.8906 47.5 19.375V30H48.75ZM32.5 10V17.5H44.4531C44.375 17.3438 44.2188 17.1094 44.0625 16.9531L38.5156 10.4688C38.2812 10.2344 37.8906 10 37.5781 10H32.5ZM12.5 37.5C15.2344 37.5 17.5 35.3125 17.5 32.5C17.5 29.7656 15.2344 27.5 12.5 27.5C9.6875 27.5 7.5 29.7656 7.5 32.5C7.5 35.3125 9.6875 37.5 12.5 37.5ZM37.5 37.5C40.2344 37.5 42.5 35.3125 42.5 32.5C42.5 29.7656 40.2344 27.5 37.5 27.5C34.6875 27.5 32.5 29.7656 32.5 32.5C32.5 35.3125 34.6875 37.5 37.5 37.5ZM45 30V20H32.5V22.5C32.5 23.2031 31.875 23.75 31.25 23.75C30.5469 23.75 30 23.2031 30 22.5V5C30 3.67188 28.8281 2.5 27.5 2.5H5C3.59375 2.5 2.5 3.67188 2.5 5V27.5C2.5 28.9062 3.59375 30 5 30H5.39062C6.40625 27.1094 9.21875 25 12.5 25C15.7031 25 18.5156 27.1094 19.5312 30H30.3906C31.4062 27.1094 34.2188 25 37.5 25C40.7031 25 43.5156 27.1094 44.5312 30H45Z" fill="#791A4D"/>
</svg>
                </div>
            </div>
          </div>
     </div>
        </div>
    </div>
</template>
<script>
import { computed, ref, onMounted, onBeforeUnmount } from 'vue';
import { useI18n } from 'vue-i18n';
export default {
  props: {
    slogan: {
      type: String,
      required: true,
    },
    sloganAr: {
      type: String,
      required: true,
    },
    sloganIr:{
      type: String, required : true,
    }
  },
  methods:{
    updateWidth() {
      this.windowWidth = window.innerWidth;
    },
  },
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
   //   window.addEventListener('resize', this.updateWidth);
      let windowWidth = window.innerWidth;
      observer.value = new IntersectionObserver(handleIntersect, {
        threshold: windowWidth>786 ? 0.7 : 0.0,
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

    return { t, locale, currentLanguage, elementRef,animationStart }; 
  },
  mounted(){
   
  },
  computed:{
    screenWidth() {
      return this.windowWidth;
    },
  }
}
</script>
