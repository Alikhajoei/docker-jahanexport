<template>
   <div class="w-full px-[10vw] pointer-events-none">
    <div :class="['fixed w-[80vw] md:h-[3.3vw] px-[3.72vw] md:px-[1.1vw] md:w-[23.8vw] h-[10vw] bg-[#1F2120] drop-shadow-md rounded-[1vw] transition-all duration-200 z-30 flex  items-center', isOpen ? 'bottom-[10vw]': 'bottom-[-10vw]']">
        <div :class="['text-white md:text-[1vw] text-[3.2vw] w-full', currentLanguage==='ar' ? 'cairo text-right' : currentLanguage==='ir' ? 'text-right vazir' :  'montserrat text-left']">{{ ErrorMessage }}</div>
    </div>
   </div>
</template>
<script>
 
export default{
    setup(){
        const { t, locale } = useI18n();
    const currentLanguage = computed(() => locale.value);
    return { t, currentLanguage }
    },
    props:{
        isOpen : {
            type : Boolean,
            Required : true,
        },
        ErrorMessage:{
            type: String,
            Required : true,
        }
    },
} 
</script>