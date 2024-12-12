<template>
  <div class="mt-[10vw] md:mt-[0vw] px-[3.4vw] md:px-[10.8vw]">
    <div class="flex flex-col md:rtl:flex-row-reverse md:ltr:flex-row md:items-center md:space-x-[4vw] justify-center md:justify-between">
      <div :class="['ltr:ml-0 ltr:mr-0 rtl:ml-0 rtl:mr-0', currentLanguage!=='en' ? 'md:ml-[1.7vw]' : ' md:mr-[4.7vw]']">
        <div
          :class="[' mt-[10vw] md:mt-0 text-center text-[7.4vw] md:text-[2.2vw]', currentLanguage === 'ar' ? 'cairo md:text-right' : 'montserrat md:text-left']">
          {{ currentLanguage === 'ar' ? titleArabic : title }}</div>
        <div
          :class="[' md:text-[1.1vw] text-[3.7vw]   mt-[4vw] md:mt-0 md:w-[39.7vw] w-full  md:h-[8.3vw] h-[24vw] text-center', currentLanguage === 'ar' ? 'cairo md:text-right' : ' md:text-left montserrat']">
          {{ typedText }}</div>
      </div>
      <div
        :class="['w-full flex md:mt-[6vw] rtl:ml-0 ltr:ml-0  rtl:mr-0 ltr:mr-0 mt-[6vw] justify-center items-center md:h-[27.4vw] h-[65.11vw]', currentLanguage!=='en' ? 'md:mr-[1.7vw]' : 'md:ml-[1.7vw]']">
        <SkeletonLoading class="w-full h-full" />
        <img @load="loadMap"
          :class="['transition-opacity duration-150', mapLoaded ? 'h-full w-full opacity-100' : 'h-0 w-0 opacity-0']"
          :src="mapImageUrl" loading="lazy">
      </div>
    </div>
    <div
      :class="['text-[6vw] md:text-[1.6vw] w-full text-[#791A4D] md:ltr:text-left md:rtl:text-right rtl:text-center ltr:text-center md:mt-[3.47vw] mt-[9.3vw]', currentLanguage !== 'en' ? 'cairo' : 'montserrat']">
      {{ t('contactInfo') }}</div>
    <div class="w-full flex flex-col justify-center md:justify-between md:flex-row items-center md:mt-[2.2vw] mt-[7vw]">
      <a :href="locationUrl" class="flex cursor-pointer my-[3vw] md:my-0">
        <div :class="['mx-[2vw] text-[4vw] md:text-[1.1vw]', currentLanguage === 'ar' ? 'cairo' : 'montserrat']">{{
          currentLanguage === 'ar' ? locationArabic : location }}</div>
        <svg class="mx-[2vw] h-[6vw] md:h-[1.6vw] md:w-[1.6vw] w-[6vw]" width="24" height="25" viewBox="0 0 24 25"
          fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M22.4375 8.3418C22.6328 8.45898 22.75 8.6543 22.75 8.84961V20.2949C22.75 20.5684 22.5547 20.8027 22.3203 20.8809L16.1094 23.1855C16.0312 23.2246 15.9531 23.2246 15.875 23.2246C15.8359 23.2246 15.7578 23.2246 15.7188 23.2246L7.04688 20.7246L1.07031 23.1855C0.914062 23.2637 0.679688 23.2637 0.523438 23.1465C0.328125 23.0293 0.25 22.834 0.25 22.5996V11.1934C0.25 10.9199 0.40625 10.6855 0.640625 10.6074L5.32812 8.84961C5.36719 9.24023 5.48438 9.63086 5.64062 10.0605L1.5 11.623V21.7012L6.5 19.5918V15.0996C6.5 14.7871 6.77344 14.4746 7.125 14.4746C7.4375 14.4746 7.75 14.7871 7.75 15.0996V19.6309L15.25 21.7793V15.0996C15.25 14.7871 15.5234 14.4746 15.875 14.4746C16.1875 14.4746 16.5 14.7871 16.5 15.0996V21.7402L21.5 19.8652V9.78711L16.4609 11.7793C16.4609 11.7793 17.0078 10.7246 17.2422 10.0996L21.8516 8.30273C22.0469 8.22461 22.2422 8.22461 22.4375 8.3418ZM11.5 15.7246C11.1094 15.7246 10.7578 15.5684 10.5234 15.2949C9.3125 13.8105 6.5 10.1777 6.5 8.14648C6.5 5.45117 8.72656 3.22461 11.5 3.22461C14.2344 3.22461 16.5 5.45117 16.5 8.14648C16.5 10.1777 13.6484 13.8105 12.4375 15.2949C12.2031 15.5684 11.8516 15.7246 11.5 15.7246ZM11.5 4.47461C9.42969 4.47461 7.75 6.1543 7.75 8.14648C7.75 9.24023 9.23438 11.7402 11.5 14.4746C13.7266 11.7402 15.25 9.24023 15.25 8.18555C15.25 6.1543 13.5312 4.47461 11.5 4.47461ZM12.4375 8.22461C12.4375 8.77148 12.0078 9.16211 11.5 9.16211C10.9531 9.16211 10.5625 8.77148 10.5625 8.22461C10.5625 7.7168 10.9531 7.28711 11.5 7.28711C12.0078 7.28711 12.4375 7.7168 12.4375 8.22461Z"
            fill="#1F2120" />
        </svg>
      </a>
      <a :href="linkedin" class="flex cursor-pointer my-[3vw] md:my-0">
        <div :class="['mx-[2vw] text-[4vw] md:text-[1.1vw]', currentLanguage !== 'en' ? 'cairo' : 'montserrat']">linkedIn/jahanexport</div>
        <svg class="mx-[2vw] h-[6vw] md:h-[1.6vw] md:w-[1.6vw] w-[6vw]" viewBox="0 0 24 25" fill="none"
          xmlns="http://www.w3.org/2000/svg">
          <g id="linkedin-in" clip-path="url(#clip0_125_53052)">
            <path id="Vector"
              d="M6.20062 21.7241H1.84688V7.70383H6.20062V21.7241ZM4.02141 5.79133C2.62922 5.79133 1.5 4.6382 1.5 3.24602C1.5 2.5773 1.76565 1.93597 2.2385 1.46311C2.71136 0.990257 3.35269 0.724609 4.02141 0.724609C4.69012 0.724609 5.33145 0.990257 5.80431 1.46311C6.27716 1.93597 6.54281 2.5773 6.54281 3.24602C6.54281 4.6382 5.41313 5.79133 4.02141 5.79133ZM22.4953 21.7241H18.1509V14.8991C18.1509 13.2726 18.1181 11.1866 15.8873 11.1866C13.6237 11.1866 13.2769 12.9538 13.2769 14.782V21.7241H8.92781V7.70383H13.1034V9.61633H13.1644C13.7456 8.51477 15.1655 7.35227 17.2838 7.35227C21.69 7.35227 22.5 10.2538 22.5 14.0226V21.7241H22.4953Z"
              fill="#1F2120" />
          </g>
          <defs>
            <clipPath id="clip0_125_53052">
              <rect width="24" height="24" fill="white" transform="translate(0 0.724609)" />
            </clipPath>
          </defs>
        </svg>

      </a>
      <a :href="'https://wa.me/' + phoneNumber" class="flex cursor-pointer my-[3vw] md:my-0">
        <div :class="['mx-[2vw] text-[4vw] md:text-[1.1vw]', currentLanguage === 'ar' ? 'cairo' : (currentLanguage==='ir' ? 'vazir' : 'montserrat')]">{{
          phoneNumber }}</div>
        <svg class="mx-[2vw] h-[6vw] md:h-[1.6vw] md:w-[1.6vw] w-[6vw]" viewBox="0 0 24 25" fill="none"
          xmlns="http://www.w3.org/2000/svg">
          <g id="whatsapp">
            <path id="Vector"
              d="M19.3547 5.27617C17.3906 3.30742 14.775 2.22461 11.9953 2.22461C6.25781 2.22461 1.58906 6.89336 1.58906 12.6309C1.58906 14.4637 2.06719 16.2543 2.97656 17.834L1.5 23.2246L7.01719 21.7762C8.53594 22.6059 10.2469 23.0418 11.9906 23.0418H11.9953C17.7281 23.0418 22.5 18.373 22.5 12.6355C22.5 9.85586 21.3188 7.24492 19.3547 5.27617ZM11.9953 21.2887C10.4391 21.2887 8.91562 20.8715 7.58906 20.084L7.275 19.8965L4.00313 20.7543L4.875 17.5621L4.66875 17.234C3.80156 15.8559 3.34688 14.2668 3.34688 12.6309C3.34688 7.86367 7.22812 3.98242 12 3.98242C14.3109 3.98242 16.4812 4.88242 18.1125 6.51836C19.7437 8.1543 20.7469 10.3246 20.7422 12.6355C20.7422 17.4074 16.7625 21.2887 11.9953 21.2887ZM16.7391 14.8105C16.4813 14.6793 15.2016 14.0512 14.9625 13.9668C14.7234 13.8777 14.55 13.8355 14.3766 14.098C14.2031 14.3605 13.7063 14.9418 13.5516 15.1199C13.4016 15.2934 13.2469 15.3168 12.9891 15.1855C11.4609 14.4215 10.4578 13.8215 9.45 12.0918C9.18281 11.6324 9.71719 11.6652 10.2141 10.6715C10.2984 10.498 10.2562 10.348 10.1906 10.2168C10.125 10.0855 9.60469 8.80586 9.38906 8.28555C9.17813 7.7793 8.9625 7.84961 8.80313 7.84023C8.65313 7.83086 8.47969 7.83086 8.30625 7.83086C8.13281 7.83086 7.85156 7.89648 7.6125 8.1543C7.37344 8.4168 6.70312 9.04492 6.70312 10.3246C6.70312 11.6043 7.63594 12.8418 7.7625 13.0152C7.89375 13.1887 9.59531 15.8137 12.2062 16.9434C13.8562 17.6559 14.5031 17.7168 15.3281 17.5949C15.8297 17.5199 16.8656 16.9668 17.0812 16.3574C17.2969 15.748 17.2969 15.2277 17.2313 15.1199C17.1703 15.0027 16.9969 14.9371 16.7391 14.8105Z"
              fill="#1F2120" />
          </g>
        </svg>


      </a>
    </div>
    <div class="block md:flex md:flex-row w-full justify-center md:justify-between">
      <div class="md:basis-1/2">
        <div style="
    overflow: hidden;">
          <div class="mt-[5vw] translate-x-[0vw] w-[90.2vw] md:h-[25vw] h-[120vw] md:w-full md:grid grid-cols-2 gap-4">
            <div v-for="(item, key) in fields"
              :class="{ 'md:col-span-2': item.isTextArea, 'opacity-0 h-[12.5vw] md:h-[3.8vw] pointer-events-none': key == 'enteredBs' }"
              :key="key">
              <div v-if="key !== 'enteredPhoneNumber'">
                <input :tabindex="key" v-if="!item.isTextArea" :dir="currentLanguage !== 'en' ? 'rtl' : 'ltr'"
                  @focus="toggleInputState(item, true)" @blur="toggleInputState(item, false)"
                  :required="item.error.length > 0"
                  :class="['w-full invalid:border-[#BA1A1A] text-[4vw] md:text-[1.1vw] h-[12.5vw] md:h-[3.8vw] px-[4vw] md:px-[1.1vw] focus:invalid:border-[#BA1A1A] focus:border-[#791A4D] focus:border-[3px] outline-none disabled:border-[#837378] disabled:border-[1px] border-[#837378] border-[1px] rounded-[1vw]', currentLanguage === 'ar' ? 'cairo text-right' : 'montserrat text-left']"  :style="item.error.length > 0 ? { borderColor: '#BA1A1A !important' } : {}"
                  type="text" v-model="item.value" />
                <textarea :tabindex="key" rows="3" v-else :dir="currentLanguage !== 'en' ? 'rtl' : 'ltr'"
                  @focus="toggleInputState(item, true)" @blur="toggleInputState(item, false)"
                  :required="item.error.length > 0"
                  :class="['w-full md:h-[6.5vw] h-[25vw]  no-scrollbar invalid:border-[#BA1A1A] md:text-[1.1vw] text-[4vw] md:px-[1.1vw] md:pt-[1.1vw] px-[4vw] focus:border-[#791A4D] focus:border-[3px] outline-none disabled:border-[#837378] disabled:border-[1px] border-[#837378] border-[1px] rounded-[1vw]', currentLanguage === 'ar' ? 'cairo text-right' : 'montserrat text-left']"
                  type="text" v-model="item.value"></textarea>
                <div v-if="!item.isTextArea"
                  :class="[currentLanguage === 'en' ? 'justify-end' : 'justify-start', currentLanguage==='en' ? 'montserrat' : (currentLanguage==='ir' ? 'vazir' : 'cairo') , ' text-[4vw] md:text-[1.1vw] flex origin-center pointer-events-none  transition-transform duration-200', item.value.length > 0 || item.isActive ? ' opacity-100 scale-75 md:translate-y-[-4.5vw] translate-y-[-16vw] ' + (currentLanguage === 'en' ? ' translate-x-[-9vw] md:translate-x-[-1.1vw] ' : ' md:translate-x-[1.1vw] translate-x-[9vw] ') : 'opacity-30 scale-1 translate-y-[-9vw] md:translate-y-[-2.8vw] ' + (currentLanguage !== 'en' ? ' translate-x-[-4vw] md:translate-x-[-1.1vw] ' : ' md:translate-x-[1.1vw] translate-x-[4vw] ')]">
                  <div
                    :class="[item.error.length > 0 ? 'text-[#BA1A1A]' : 'text-[#1F2120]', currentLanguage !== 'en' ? 'text-right' : 'text-left', 'inline-block transition-all pointer-events-none ease-in-out duration-200', item.value.length > 0 || item.isActive ? 'bg-[#fdf8f8]' : 'bg-[#fdf8f800]']">
                    {{ t(item.title) }}</div>
                </div>
                <div v-else
                  :class="[currentLanguage === 'en' ? ' justify-end' : '  justify-start', currentLanguage==='en' ? 'montserrat' : (currentLanguage==='ir' ? 'vazir' : 'cairo'), ' text-[4vw] md:text-[1.1vw] flex origin-center pointer-events-none  transition-transform duration-200', item.value.length > 0 || item.isActive ? 'opacity-100 scale-75 md:translate-y-[-7.7vw] translate-y-[-30vw]' + (currentLanguage === 'en' ? ' translate-x-[-3.7vw]' : ' translate-x-[3.7vw]') : 'opacity-30 scale-1 translate-y-[-23vw] md:translate-y-[-6vw] ' + (currentLanguage !== 'en' ? 'translate-x-[-4vw] md:translate-x-[-1.1vw]' : 'md:translate-x-[1.1vw] translate-x-[4vw]')]">
                  <div
                    :class="[item.error.length > 0 ? 'text-[#BA1A1A]' : 'text-[#1F2120]', currentLanguage !== 'en' ? 'text-right' : 'text-left', 'inline-block transition-all pointer-events-none ease-in-out duration-200', item.value.length > 0 || item.isActive ? 'bg-[#fdf8f8]' : 'bg-[#fdf8f800]']">
                    {{ t(item.title) }}</div>
                </div>
                <div
                  :class="['flex pointer-events-none items-center absolute rtl:left-[6vw] -translate-y-[15vw] w-[90vw] text-white justify-end']">
                  <!-- <svg :class="['w-[6vw] h-[6vw] cursor-pointer transition-all duration-200 ease-out',item.error.length > 0 ? 'scale-100' : 'scale-0',currentLanguage==='ar' ? ' -translate-x-[6vw]':'translate-x-[73vw]']" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 17C12.2833 17 12.5208 16.9042 12.7125 16.7125C12.9042 16.5208 13 16.2833 13 16C13 15.7167 12.9042 15.4792 12.7125 15.2875C12.5208 15.0958 12.2833 15 12 15C11.7167 15 11.4792 15.0958 11.2875 15.2875C11.0958 15.4792 11 15.7167 11 16C11 16.2833 11.0958 16.5208 11.2875 16.7125C11.4792 16.9042 11.7167 17 12 17ZM11 13H13V7H11V13ZM12 22C10.6167 22 9.31667 21.7375 8.1 21.2125C6.88333 20.6875 5.825 19.975 4.925 19.075C4.025 18.175 3.3125 17.1167 2.7875 15.9C2.2625 14.6833 2 13.3833 2 12C2 10.6167 2.2625 9.31667 2.7875 8.1C3.3125 6.88333 4.025 5.825 4.925 4.925C5.825 4.025 6.88333 3.3125 8.1 2.7875C9.31667 2.2625 10.6167 2 12 2C13.3833 2 14.6833 2.2625 15.9 2.7875C17.1167 3.3125 18.175 4.025 19.075 4.925C19.975 5.825 20.6875 6.88333 21.2125 8.1C21.7375 9.31667 22 10.6167 22 12C22 13.3833 21.7375 14.6833 21.2125 15.9C20.6875 17.1167 19.975 18.175 19.075 19.075C18.175 19.975 17.1167 20.6875 15.9 21.2125C14.6833 21.7375 13.3833 22 12 22Z" fill="#BA1A1A"/>
                </svg> -->
                </div>
                <div
                  :class="['w-full pointer-events-none -translate-y-[5vw] md:translate-y-[-1.5vw] text-[3vw] md:text-[0.8vw] text-[#BA1A1A]', currentLanguage === 'ar' ? ' translate-x-[-2vw] text-right' : ' translate-x-[2vw] text-left', currentLanguage==='en' ? 'montserrat' : (currentLanguage==='ir' ? 'vazir' : 'cairo')]">
                  {{ currentLanguage === 'ar' ? item.errorArabic : (currentLanguage==='ir' ? item.errorPersian :item.error) }}</div>

              </div>
              <div v-else>
                <input :tabindex="key" v-if="!item.isTextArea" :dir="currentLanguage !== 'en' ? 'rtl' : 'ltr'"
                  @focus="toggleInputState(item, true)" @blur="toggleInputState(item, false)"
                  :required="item.error.length > 0"
                  :class="['w-full invalid:border-[#BA1A1A] text-[4vw] md:text-[1.1vw] h-[12.5vw] md:h-[3.8vw] pl-[20vw] md:pl-[7vw] pr-[4vw] md:px-[1.1vw] focus:invalid:border-[#BA1A1A] focus:border-[#791A4D] focus:border-[3px] outline-none disabled:border-[#837378] disabled:border-[1px] border-[#837378] border-[1px] rounded-[1vw]', currentLanguage !== 'en' ? ' text-right' : ' text-left', currentLanguage === 'ar' ?'cairo' : (currentLanguage==='ir' ? 'vazir' : 'montserrat') ]"
                  type="text" v-model="formattedNumber" />
                <textarea :tabindex="key" rows="3" v-else :dir="currentLanguage !== 'en' ? 'rtl' : 'ltr'"
                  @focus="toggleInputState(item, true)" @blur="toggleInputState(item, false)"
                  :required="item.error.length > 0"
                  :class="['w-full md:h-[6.5vw] h-[25vw]  no-scrollbar invalid:border-[#BA1A1A] md:text-[1.1vw] text-[4vw] md:px-[1.1vw] md:pt-[1.1vw] px-[4vw] focus:border-[#791A4D] focus:border-[3px] outline-none disabled:border-[#837378] disabled:border-[1px] border-[#837378] border-[1px] rounded-[1vw]', currentLanguage !== 'en' ? ' text-right' : ' text-left', currentLanguage==='ar' ? 'cairo' : (currentLanguage==='ir'? 'vazir' : 'montserrat')]"
                  type="text" v-model="item.value"></textarea>

                <div v-if="!item.isTextArea"
                  :class="[currentLanguage === 'en' ? ' justify-end' : '  justify-start', currentLanguage==='ar' ? 'cairo' : (currentLanguage==='ir' ? 'vazir' : 'montserrat'), ' text-[4vw] md:text-[1.1vw] flex origin-center pointer-events-none  transition-transform duration-200', item.value.length > 0 || item.isActive ? ' opacity-100 scale-75 md:translate-y-[-4.5vw] translate-y-[-16vw] ' + (currentLanguage === 'en' ? ' translate-x-[8vw] md:translate-x-[4vw] ' : ' md:translate-x-[-3vw] translate-x-[0vw] ') : 'opacity-30 scale-1 translate-y-[-9vw] md:translate-y-[-2.8vw] ' + (currentLanguage !== 'en' ? ' translate-x-[-49vw] md:translate-x-[-4.1vw] ' : ' md:translate-x-[8.1vw] translate-x-[22vw] ')]">
                  <div
                    :class="[item.error.length > 0 ? 'text-[#BA1A1A]' : 'text-[#1F2120]', currentLanguage !== 'en' ? 'text-right' : 'text-left', 'inline-block transition-all pointer-events-none ease-in-out duration-200', item.value.length > 0 || item.isActive ? 'bg-[#fdf8f8]' : 'bg-[#fdf8f800]']">
                    {{ t(item.title) }}</div>
                </div>
                <div v-else
                  :class="[currentLanguage === 'en' ? 'montserrat' : (currentLanguage==='ir' ? 'vazir' : 'montserrat'), ' text-[4vw] justify-end md:text-[1.1vw] flex origin-center pointer-events-none  transition-transform duration-200', item.value.length > 0 || item.isActive ? 'opacity-100 scale-75 md:translate-y-[-7.7vw] translate-y-[-30vw]' + (currentLanguage === 'en' ? ' translate-x-[-3.7vw]' : ' translate-x-[-3.7vw]') : 'opacity-30 scale-1 translate-y-[-23vw] md:translate-y-[-6vw] ' + (currentLanguage !== 'en' ? 'translate-x-[4vw] md:translate-x-[-1.1vw]' : 'md:translate-x-[1.1vw] translate-x-[4vw]')]">
                  <div
                    :class="[item.error.length > 0 ? 'text-[#BA1A1A]' : 'text-[#1F2120]', currentLanguage !== 'en' ? 'text-right' : 'text-left', 'inline-block transition-all pointer-events-none ease-in-out duration-200', item.value.length > 0 || item.isActive ? 'bg-[#fdf8f8]' : 'bg-[#fdf8f800]']">
                    {{ t(item.title) }}</div>
                </div>
                <div
                  :class="['w-[17.7vw] select-none z-10 absolute md:translate-y-[-5vw] translate-y-[-18vw] flex justify-between items-center md:w-[6vw] md:h-[3vw] h-[11.5vw] cursor-pointer bg-white left-0 md:translate-x-[1vw] translate-x-[2vw]']">
                  <svg @click.self="toggleCountriesList"
                    :class="[countriesOpen ? 'rotate-0' : 'rotate-180', 'h-[4.65vw] md:w-[1.38vw] md:h-[1.38vw] w-[4.65vw]', 'transition-all duration-200']"
                    viewBox="0 0 21 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g id="Icon">
                      <path id="icon" d="M5.99902 11.6667L10.1657 7.5L14.3324 11.6667H5.99902Z" fill="#1F2120" />
                    </g>
                  </svg>
                  <div @click.self="toggleCountriesList"
                    :class="[currentLanguage === 'ar' ? 'cairo' :(currentLanguage==='ir' ? 'vazir' : 'montserrat'), 'text-[3.7vw] md:text-[1.1vw] mx-[0.2vw]']"
                    v-if="countriesFetched">{{ countries[chosenCountry].dialCode }}</div>
                  <img @click.self="toggleCountriesList"
                    class="w-[4.8vw] md:w-[1.5vw] md:h-[1.1vw] h-[3.7vw] mx-[0.2vw]"
                    :src="countries[chosenCountry].flag" v-if="countriesFetched">
                  <div>
                  </div>
                  <div
                    :class="[' overflow-y-scroll country-list bg-white rounded-sm absolute z-20 md:translate-y-[7vw] translate-y-[27vw] origin-top h-[40vw] md:h-[10vw] md:w-[18.3vw] w-[60vw] md:translate-x-[12vw] translate-x-[40vw] transition-all duration-200', countriesOpen ? ' pointer-events-auto opacity-100' : 'opacity-0 pointer-events-none ']">
                    <div @click="selectCountry(index)"
                      class="w-full pt-[1.8vw] md:pt-[0.8vw] px-[4vw] md:px-[1.1vw] bg-white hover:bg-[#FFE6ED] transition-colors duration-200 cursor-pointer"
                      v-for="(item, index) in countries" :key="index">
                      <div
                        class="flex space-x-[2vw] md:space-x-[0.8vw] md:pb-[0.8vw] pb-[1.8vw] md:justify-between justify-between items-center w-full">
                        <div
                          :class="[currentLanguage === 'ar' ? 'cairo' : (currentLanguage==='ir' ? 'vazir' : 'montserrat'), 'text-[2.7vw] md:text-[0.7vw] md:mx-[0.3vw] mx-[1vw] basis-1/2']">
                          {{ currentLanguage === 'en' ? item.name : (currentLanguage==='ir' ? item.persianName : item.arabicName) }}</div>
                        <div class="flex space-x-[2vw] md:space-x-[0.8vw]">
                          <div
                            :class="[currentLanguage === 'ar' ? 'cairo' : (currentLanguage==='ir' ?'vazir' : 'montserrat'), 'text-[2.7vw] md:text-[0.7vw] md:mx-[0.3vw] mx-[1vw] basis-1/4']">
                            {{ item.dialCode }}</div>
                          <img :src="item.flag" class="w-[4.8vw] md:w-[1.45vw] md:h-[1.1vw] h-[3.7vw] basis-1/4">
                        </div>
                      </div>
                      <div class="w-full h-[1px] bg-[#D9C6CB]"></div>
                    </div>
                  </div>

                </div>
                <div
                  :class="['flex pointer-events-none items-center absolute rtl:left-[6vw] -translate-y-[15vw] w-[90vw] text-white justify-end']">
                  <!-- <svg :class="['w-[6vw] h-[6vw] cursor-pointer transition-all duration-200 ease-out',item.error.length > 0 ? 'scale-100' : 'scale-0',currentLanguage==='ar' ? ' -translate-x-[6vw]':'translate-x-[73vw]']" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 17C12.2833 17 12.5208 16.9042 12.7125 16.7125C12.9042 16.5208 13 16.2833 13 16C13 15.7167 12.9042 15.4792 12.7125 15.2875C12.5208 15.0958 12.2833 15 12 15C11.7167 15 11.4792 15.0958 11.2875 15.2875C11.0958 15.4792 11 15.7167 11 16C11 16.2833 11.0958 16.5208 11.2875 16.7125C11.4792 16.9042 11.7167 17 12 17ZM11 13H13V7H11V13ZM12 22C10.6167 22 9.31667 21.7375 8.1 21.2125C6.88333 20.6875 5.825 19.975 4.925 19.075C4.025 18.175 3.3125 17.1167 2.7875 15.9C2.2625 14.6833 2 13.3833 2 12C2 10.6167 2.2625 9.31667 2.7875 8.1C3.3125 6.88333 4.025 5.825 4.925 4.925C5.825 4.025 6.88333 3.3125 8.1 2.7875C9.31667 2.2625 10.6167 2 12 2C13.3833 2 14.6833 2.2625 15.9 2.7875C17.1167 3.3125 18.175 4.025 19.075 4.925C19.975 5.825 20.6875 6.88333 21.2125 8.1C21.7375 9.31667 22 10.6167 22 12C22 13.3833 21.7375 14.6833 21.2125 15.9C20.6875 17.1167 19.975 18.175 19.075 19.075C18.175 19.975 17.1167 20.6875 15.9 21.2125C14.6833 21.7375 13.3833 22 12 22Z" fill="#BA1A1A"/>
                </svg> -->
                </div>
                <div
                  :class="['w-full pointer-events-none -translate-y-[5vw] md:translate-y-[-1.5vw]  text-[3vw] md:text-[0.8vw] text-[#BA1A1A]', currentLanguage !== 'en' ? ' translate-x-[-2vw] text-right' : ' translate-x-[2vw] text-left', currentLanguage==='ar' ? 'cairo' : (currentLanguage==='ir' ? 'vazir' : 'montserrat')]">
                  {{ currentLanguage === 'ar' ? item.errorArabic : (currentLanguage==='ir' ? item.errorPersian : item.error) }}</div>

              </div>
            </div>
          </div>
        </div>
        <div class="flex justify-center items-center">
          <div @click="validateFields"
            :class="['mt-[0vw]  mb-[10vw] select-none cursor-pointer py-[2.5vw] md:py-[0.7vw] flex justify-center items-center w-full md:w-[13.4vw] rounded-full bg-[#791A4D] hover:bg-[#521334] transition-all duration-200']">
            <div v-if="!isSending" :class="[currentLanguage === 'ar' ? 'cairo' : (currentLanguage==='ir' ?'vazir' : 'montserrat ') , ' text-white  text-[3.5vw] md:text-[1vw]']">
              {{ t('sendMessage') }}
            </div>
            <div  v-else>
              <LoadingSpinner class="h-full w-full"/>
            </div>
          </div>
        </div>
      </div>
      <div
        class="w-full mb-[10vw] md:basis-1/2 flex flex-col  rtl:ml-0 ltr:ml-0 rounded-[3vw] md:rtl:mr-[1.7vw] rtl:mr-0 ltr:mr-0 md:ltr:ml-[1.7vw] md:mt-[5vw] mt-[6vw] justify-center items-center md:h-[24.8vw] md:w-[37.2vw] h-[65.11vw]">
        <SkeletonLoading class="w-full rounded-[3vw] h-full" />
        <NuxtImg @load="loadImage"
          :class="['transition-opacity object-cover rounded-[3vw] duration-150', imageLoaded ? 'h-full w-full opacity-100' : 'h-0 w-0 opacity-0']"
          :src="imageUrl" loading="lazy"/>
      </div>
    </div>
<SnackBar :isOpen="snackBarState" :ErrorMessage="currentLanguage==='ar' ? arabicSnackBarMessage : (currentLanguage==='ir' ? persianSnackBarMessage : snackBarMessage)" class="w-full flex justify-center items-center"/>
  </div>

</template>

<script>
import { loadingStore } from '~/store/loading-state.js'
import { footerStore } from '~/store/footer-state';
import SkeletonLoading from '../components/global/SkeletonLoading.vue';
import LoadingSpinner from '~/components/global/LoadingSpinner.vue';
import SnackBar from '~/components/global/SnackBar.vue';
export default {
  setup() {
    const { t, locale } = useI18n();
    const currentLanguage = computed(() => locale.value);
    return { t, currentLanguage }
  },
  mounted() {
    this.fetchCountryData()
    this.loadingState.setLoading(true)
   this.fetchData()
   useHead({
      title: this.t('jahanExport') + " | " + this.t('contactUs')
    });
  },
  computed: {
    isFormFilled() {
      return Object.values(this.fields).every(field => field.value.length > 0);
    }
  },
  methods: {
    fetchData(){
      fetch('https://admin.jahanexport.com/contact-us/api/')
        .then(response => response.text())
        .then(text => {
          try {
           const data = JSON.parse(text);
this.loadingState.setLoading(false);
          this.imageUrl = data[data.length - 1]?.footer?.image_url;
           this.mapImageUrl = data[data.length - 1]?.footer?.map_image_url;
         this.title = data[data.length -1]?.footer.title
         this.titleArabic = data[data.length-1]?.footer.title_arabic;
         this.titlePersian = data[data.length-1]?.footer.title_persian;
         this.about = data[data.length-1]?.footer.about
         this.aboutArabic = data[data.length-1]?.footer.about_arabic;
         this.aboutPersian = data[data.length-1]?.footer.about_persian;
           this.typeText();
          } catch (error) {
            this.loadingState.setLoading(false);
            console.error('JSON Parsing Error:', error);
             this.$router.push('/notFound');
          }
        })
        .catch(error => {
          this.loadingState.setLoading(false);
          console.error('Error fetching data:', error);
           this.$router.push('/notFound');
        });
    },
    toggleCountriesList() {
      this.countriesOpen = !this.countriesOpen
    },
    selectCountry(index) {
      this.chosenCountry = index;
      this.countriesOpen = false;
    },
    loadMap() {
      this.mapLoaded = true;
    },
    loadImage() {
      this.imageLoaded = true;
    },
    toggleInputState(data, state) {
      data.isActive = state
      this.countriesOpen = false;
    },
    validateFields() {
  let isValid = true;

  // Validate each field for empty values
  if (this.fields.enteredName.value.trim() === '') {
    this.fields.enteredName.error = 'This field should not be empty';
    this.fields.enteredName.errorArabic = 'يجب ألا يكون هذا الحقل فارغاً';
    this.fields.enteredMessage.errorPersian = 'این فیلد الزامیست'
    isValid = false;
  } else {
    this.fields.enteredName.error = '';
    this.fields.enteredName.errorArabic = '';
    this.fields.enteredMessage.errorPersian = ''
  }

  if (this.fields.enteredLastName.value.trim() === '') {
    this.fields.enteredLastName.error = 'This field should not be empty';
    this.fields.enteredLastName.errorArabic = 'يجب ألا يكون هذا الحقل فارغاً';
    this.fields.enteredMessage.errorPersian = 'این فیلد الزامیست'
    isValid = false;
  } else {
    this.fields.enteredLastName.error = '';
    this.fields.enteredLastName.errorArabic = ''
    this.fields.enteredMessage.errorPersian = ''

  }

  if (this.fields.enteredPhoneNumber.value.trim() === '') {
    this.fields.enteredPhoneNumber.error = 'This field should not be empty';
    this.fields.enteredPhoneNumber.errorArabic = 'يجب ألا يكون هذا الحقل فارغاً';
    this.fields.enteredMessage.errorPersian = 'این فیلد الزامیست'
    isValid = false;
  } else {
    this.fields.enteredPhoneNumber.error = '';
    this.fields.enteredPhoneNumber.errorArabic = '';
    this.fields.enteredMessage.errorPersian = ''
  }

  if (this.fields.enteredMessage.value.trim() === '') {
    this.fields.enteredMessage.error = 'This field should not be empty';
    this.fields.enteredMessage.errorArabic = 'يجب ألا يكون هذا الحقل فارغاً';
    this.fields.enteredMessage.errorPersian = 'این فیلد الزامیست'
    isValid = false;
  } else {
    this.fields.enteredMessage.error = '';
    this.fields.enteredMessage.errorArabic = '';
    this.fields.enteredMessage.errorPersian = ''
  }
  const emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  if (this.fields.enteredEmail.value && !emailPattern.test(this.fields.enteredEmail.value.trim())) {
    this.fields.enteredEmail.error = 'Invalid email address';
    this.fields.enteredEmail.errorArabic = 'عنوان البريد الإلكتروني غير صالح';
    this.fields.enteredEmail.errorPersian = 'آدرس ایمیل معتبر نمیباشد'
    isValid = false;
  } else if (this.fields.enteredEmail.value.trim() === '') {
    this.fields.enteredEmail.error = 'This field should not be empty';
    this.fields.enteredEmail.errorArabic = 'يجب ألا يكون هذا الحقل فارغاً';
    this.fields.enteredEmail.errorPersian = 'این فیلد الزامیست'
        isValid = false;
  } else {
    this.fields.enteredEmail.error=''
    this.fields.enteredEmail.errorArabic=''
    this.fields.enteredMessage.errorPersian = ''
  }

  if (isValid) {
   this.sendMessage()
  }

},
async sendMessage(){
         const formData = new FormData();
      formData.append("first_name", this.fields.enteredName.value);
      formData.append("last_name", this.fields.enteredLastName.value);
      formData.append("email_address", this.fields.enteredEmail.value);
      formData.append("phone_number",this.countries[this.chosenCountry].dialCode +  this.fields.enteredPhoneNumber.value);
      formData.append("message", this.fields.enteredMessage.value);

      this.isSending = true;
      try {
        const response = await fetch("https://admin.jahanexport.com/contact-us/", {
          method: "POST",
          body: formData,
        });

        // Handle the response
        if (response.ok) {
          this.isSending = false;
          this.openSnackbar()
          this.snackBarMessage = 'Message sent successfully'
          this.arabicSnackBarMessage = 'تم إرسال الرسالة بنجاح'
          this.persianSnackBarMessage = 'پیام شما با موفقیت ارسال شد'
          for (const key in this.fields) {
    if (this.fields.hasOwnProperty(key)) {
      this.fields[key].value = '';
      this.fields[key].error = '';
      this.fields[key].errorArabic = '';
      this.fields[key].errorPersian = ''
    }
  }
        } else {
          console.error("Form submission failed.", response.status);
          this.isSending = false;
          this.snackBarMessage = 'A problem occurred, please try again later'
          this.arabicSnackBarMessage = 'حدثت مشكلة، يرجى المحاولة مرة أخرى لاحقاً';
          this.persianSnackBarMessage = 'مشکلی پیش آمده، لطفا دوباره امتحان کنید'
          this.openSnackbar()
        }
      } catch (error) {
        console.error("Error:", error);
        this.isSending = false;
        this.snackBarMessage = 'A problem occurred, please try again later'
        this.arabicSnackBarMessage = 'حدثت مشكلة، يرجى المحاولة مرة أخرى لاحقاً';
        this.persianSnackBarMessage = 'مشکلی پیش آمده، لطفا دوباره امتحان کنید'
        this.persianSnackBarMessage
        this.openSnackbar()
      }
},
    clearInput(item) {
      item.value = ''
    },
  async fetchCountryData() {
    try {
      const response = await fetch('https://restcountries.com/v3.1/all');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const countryList = data.map(country => ({
        name: country.name.common,
        arabicName: country.translations?.ara?.common || "N/A",
        persianName: country.translations?.per?.common || "N/A", // Retrieve Arabic name if available
        flag: country.flags.svg,
        dialCode: country.idd.root + (country.idd.suffixes ? country.idd.suffixes[0] : ''),
      }));

      // Sort countries alphabetically by name
      countryList.sort((a, b) => a.name.localeCompare(b.name));
      this.countriesFetched = true;
      this.countries = countryList;
    } catch (error) {
      this.countriesFetched = false;
      console.error('Error fetching country data:', error);
    }
  },
    openSnackbar(){
      this.snackBarState = true;
      setTimeout(()=>{
        this.snackBarState = false;
      },this.snackBarTime)
    },
    typeText() {
      let index = 0;
      if (this.currentLanguage === 'ar') {
        const typingInterval = setInterval(() => {

          if (index < this.aboutArabic.length) {
            this.typedText += this.aboutArabic[index];
            index++;
          } else {
            clearInterval(typingInterval);
          }
        }, 0.1);
      } else if(this.currentLanguage==='ir'){
        const typingInterval = setInterval(() => {

if (index < this.aboutPersian.length) {
  this.typedText += this.aboutPersian[index];
  index++;
} else {
  clearInterval(typingInterval);
}
}, 0.1);
      } else {
        const typingInterval = setInterval(() => {

          if (index < this.about.length) {
            this.typedText += this.about[index];
            index++;
          } else {
            clearInterval(typingInterval);
          }
        }, 20);
      }

    },
  },
  components: {
    SkeletonLoading,
    LoadingSpinner,
    SnackBar,
  },
  watch: {
    fields: {
      handler(oldfields,newFields) {
         if(oldfields.enteredEmail.value !== newFields.enteredEmail.value){
            this.fields.enteredEmail.errorArabic = ''
            this.fields.enteredEmail.error = ''
            this.fields.enteredEmail.errorPersian = ''
         }
        if(newFields.enteredName.value !==''){
          this.fields.enteredName.error=''
          this.fields.enteredName.errorArabic = ''
          this.fields.enteredName.errorPersian = ''
        }
        if(newFields.enteredLastName.value!==''){
          this.fields.enteredLastName.error=''
          this.fields.enteredLastName.errorArabic = ''
          this.fields.enteredLastName.errorPersian = ''
        }
        if(newFields.enteredPhoneNumber.value !==''){
          this.fields.enteredPhoneNumber.error = ''
          this.fields.enteredPhoneNumber.errorArabic = ''
          this.fields.enteredPhoneNumber.errorPersian = ''
        }
        if(newFields.enteredMessage.value!==''){
          this.fields.enteredMessage.error=''
          this.fields.enteredMessage.errorArabic =''
          this.fields.enteredMessage.errorPersian = ''
        }
      },
      deep: true
    }
  },
  data() {
    return {
      footerState: footerStore(),
      countriesFetched: false,
      countries: [],
      chosenCountry: 0,
      countriesOpen: false,
      imageLoaded: false,
      isSending:false,
      snackBarState : false,
      snackBarTime:2500,
      arabicSnackBarMessage:'',
      persianSnackBarMessage:'',
      snackBarMessage:'',
      fields: {
        enteredName: {
          value: '',
          isActive: false,
          error: '',
          errorArabic: '',
          isTextArea: false,
          title: 'firstName',
          errorPersian:'',
        },
        enteredLastName: {
          value: '',
          isActive: false,
          error: '',
          errorArabic: '',
          isTextArea: false,
          title: 'lastName',
          errorPersian:'',
        },
        enteredEmail: {
          value: '',
          isActive: false,
          error: '',
          errorArabic: '',
          isTextArea: false,
          title: 'emailAddress',
          errorPersian:'',
        },
        enteredPhoneNumber: {
          value: '',
          isActive: false,
          error: '',
          errorArabic: '',
          isTextArea: false,
          title: 'phoneNumber',
          errorPersian:'',
        },
        enteredMessage: {
          value: '',
          isActive: false,
          error: '',
          errorArabic: '',
          isTextArea: true,
          title: 'message',
          errorPersian:'',
        }
      },
      typedText: "",
      loadingState: loadingStore(),
      title: '',
      about: '',
      titleArabic: '',
      aboutArabic: '',
      titlePersian: '',
      aboutPersian:'',
      imageUrl: '',
      mapImageUrl: '',
      mapLoaded: false,
      imageLoaded: false,
    }
  },
  computed: {
    phoneNumber(){
      return this.footerState.phoneNumber
    },
    linkedin(){
      return this.footerState.linkedin
    },
    locationArabic(){
      return this.footerState.addressArabic
    },
    location(){
       return this.footerState.address
    },
    locationUrl(){
       return this.footerState.locationUrl
    },
    formattedNumber: {
      get() {
        return this.fields.enteredPhoneNumber.value.replace(/(\d{3})(?=\d)/g, '$1 ').trim();
      },
      set(value) {
        this.fields.enteredPhoneNumber.value = value.replace(/\D/g, ''); // Remove any non-numeric characters
      }
    },
    emailError(){
      return this.fields.enteredEmail.error
    }
  }
}
</script>
<style>
.no-scrollbar {
  resize: none;
  overflow: hidden;
}

::-webkit-scrollbar {
  width: 4px;
}

/* Track */
::-webkit-scrollbar-track {
  background: transparent;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
}

.country-list {
  will-change: opacity;
  box-shadow: 0px 2px 6px 0px rgba(0, 0, 0, 0.15), 0px 1px 2px 0px rgba(0, 0, 0, 0.30);
}
</style>