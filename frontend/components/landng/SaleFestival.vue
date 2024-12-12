<template>
    <div ref="elementRef" :class="['mt-[25vw] cursor-default select-none justify-between items-center flex flex-col md:flex-row md:mt-[5.5vw] md:px-[10.8vw] px-[3.75vw]', currentLanguage==='ar' ? 'cairo': currentLanguage==='ir' ? 'vazir' : 'montserrat']">
<div class="w-full md:w-[39.2vw]">
    <div :class="['text-center md:rtl:text-right md:ltr:text-left  md:text-[3.95vw] text-[10.8vw] transition-all duration-200 ease-out ', animationStart ? 'rtl:translate-x-0 ltr:translate-x-0 opacity-100':'ltr:translate-x-[-7vw] rtl:translate-x-[7vw] opacity-0']">{{ currentLanguage==='ar' ? saleFestival.titleAr : currentLanguage==='ir' ? saleFestival.titleIr : saleFestival.title }}</div>
    <div :class="['text-center md:rtl:text-right md:ltr:text-left  text-[5.1vw] md:text-[1.7vw] transition-all duration-200 ease-out delay-150', animationStart ? 'opacity-100 rtl:translate-x-0 ltr:translate-x-0' : 'opacity-0 ltr:translate-x-[-7vw] rtl:translate-x-[7vw]']">{{  currentLanguage ==='ar' ? saleFestival.captionAr : currentLanguage==='ir'? saleFestival.captionIr :  saleFestival.caption }}</div>
</div>
<div :class="['mt-[8vw] md:mt-[2vw] bg-[#791A4D] pt-[8vw] md:pt-[5.2vw] h-[105vw] md:h-[39.1vw] md:w-[32vw] w-full rounded-full delay-300 transition-all duration-500 ease-out', animationStart ? 'opacity-100 scale-100' :'opacity-0 scale-0']">
    <div class="flex w-full justify-start">
        <div :class="['w-[26.5vw] h-[26.5vw] md:h-[10.5vw] md:w-[10.5vw] flex flex-col justify-center items-center rtl:translate-x-0 ltr:translate-x-0 md:rtl:translate-x-[4vw] md:ltr:-translate-x-[4vw]  drop-shadow-md relative z-10 bg-white rounded-full delay-700 transition-all duration-200 ease-out', animationStart ? 'scale-100' : 'scale-0']">
            <div class="text-[10.4vw] md:text-[3.95vw] text-center">{{ saleFestival.discount }}%</div>
            <div class="text-[3.7vw] md:text-[1.6vw] text-center">{{ t('discount') }}</div>
        </div>
    </div>
    <NuxtImg :src="saleFestival.imageUrl" :class="['w-[60vw] translate-x-[-16vw] md:translate-x-0 h-[60vw] md:w-[25vw] md:h-[25vw] md:-translate-y-[10vw] self-center translate-y-[-10vw] justify-self-center transition-all duration-500 delay-300',animationStart ? 'opacity-100':'opacity-0' ]"/>
</div>
</div>
</template>

<script>

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
        threshold: 0.5,
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
  props: {
    saleFestival: {
      type: Object,
      required: true,
      default: () => ({
        imageUrl: '',
        discount: '',
        title: '',
        titleAr: '',
        caption: '',
        captionAr: '',
        titleIr: '',
        captionIr: ''
      }),
      validator: (value) => {
        return (
          typeof value.imageUrl === 'string' &&
          typeof value.discount === 'string' &&
          typeof value.title === 'string' &&
          typeof value.titleAr === 'string' &&
          typeof value.caption === 'string' &&
          typeof value.captionAr === 'string' && 
          typeof value.titleIr === 'string' &&
          typeof value.captionIr === 'string'
        );
      }
    }
  }
}
</script>