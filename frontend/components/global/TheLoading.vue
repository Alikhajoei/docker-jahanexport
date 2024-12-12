<template>
    <div class="w-[100vw] h-[100vh] flex-col fixed z-[99] top-0 bg-[#FDF8F8] flex justify-center items-center">
        <span class="loader"></span>
<div :class="['mt-[3vw] text-[6vw] md:text-[2vw]', currentLanguage==='ar' ? 'cairo' : currentLanguage==='ir' ? 'vazir' : 'montserrat']">{{t('pleaseWait')}}</div>
    </div>
</template>
<script>
export default{
    setup(){
        const { t, locale } = useI18n();
        const currentLanguage = computed(() => locale.value);
        return { t, locale, currentLanguage}; 
    },
}
</script>
<style scoped>
.loader {
  position: relative;
  width: 130px;
  height: 100px;
  background-repeat: no-repeat;
  background-image: linear-gradient(#791A4D, #791A4D),
  linear-gradient(#FFB0CF, #FFB0CF), linear-gradient(#FFB0CF, #FFB0CF);
  background-size: 80px 70px, 30px 50px, 30px 30px;
  background-position: 0 0, 80px 20px, 100px 40px;
}
.loader:after {
  content: "";
  position: absolute;
  bottom: 10px;
  left: 12px;
  width: 10px;
  height: 10px;
  background: #fff;
  border-radius: 50%;
  box-sizing: content-box;
  border: 10px solid #000;
  box-shadow: 78px 0 0 -10px #fff, 78px 0 #000;
  animation: wheelSk 0.75s ease-in infinite alternate;
}

.loader:before {
  content: "";
  position: absolute;
  right: 100%;
  top: 0px;
  height: 70px;
  width: 70px;
  background-image: linear-gradient(#fff 45px, transparent 0),
    linear-gradient(#fff 45px, transparent 0),
    linear-gradient(#fff 45px, transparent 0);
  background-repeat: no-repeat;
  background-size: 30px 4px;
  background-position: 0px 11px, 8px 35px, 0px 60px;
  animation: lineDropping 0.75s linear infinite;
}

@keyframes wheelSk {
  0%, 50%, 100% { transform: translatey(0) }
  30%, 90% { transform: translatey(-3px) }
}

@keyframes lineDropping {
  0% {
    background-position: 100px 11px, 115px 35px, 105px 60px;
    opacity: 1;
  }
  50% { background-position: 0px 11px, 20px 35px, 5px 60px }
  60% { background-position: -30px 11px, 0px 35px, -10px 60px }
  75%, 100% {
    background-position: -30px 11px, -30px 35px, -30px 60px;
    opacity: 0;
  }
}

</style>