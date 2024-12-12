<template>
    <div class="select-none fixed z-50 top-0 ">
        <div
            :class="{ 'w-full bg-[#FDF8F8] flex justify-between items-center px-[3.75vw] md:px-[7.7vw] py-[2.7vw] ': true, 'montserrat': currentLanguage === 'en', 'cairo': currentLanguage === 'ar' ,'vazir' :  currentLanguage==='ir'  }">
            <div @click="toggleDrawer" class="block md:hidden cursor-pointer">
                <svg width="6vw" height="6vw" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g id="Icon">
                        <path id="icon" d="M3 18V16H21V18H3ZM3 13V11H21V13H3ZM3 8V6H21V8H3Z" fill="#1F2120" />
                    </g>
                </svg>
            </div>
            <div class="block md:hidden text-[5.5vw]">{{ currentRouteTitle }}</div>
            <NuxtLink class="h-full flex space-x-[1.6vw] justify-center items-center cursor-pointer" to="/">
                <svg id="Layer_2" class="md:w-[6.5vw] h-[12vw] w-[12vw] md:h-[6.2vw]" data-name="Layer 2"
                    xmlns="http://www.w3.org/2000/svg" viewBox="0 0 223.19 215.27">
                    <defs>

                    </defs>
                    <g id="Layer_1-2" data-name="Layer 1">
                        <g>
                            <path class="cls-2"
                                d="M111.6,189.36c-45.07,0-81.73-36.66-81.73-81.73S66.53,25.91,111.6,25.91s81.73,36.66,81.73,81.73-36.66,81.73-81.73,81.73ZM111.6,53.01c-30.12,0-54.63,24.51-54.63,54.63s24.51,54.63,54.63,54.63,54.63-24.51,54.63-54.63-24.51-54.63-54.63-54.63Z" />
                            <path class="cls-1"
                                d="M108.5,215.27c-1.2-21.99.84-44.11,4.81-65.71,10.02-54.13,36.84-106.43,85.4-135.17,7.79-4.72,16.06-8.69,24.48-12.09-4.48,2.61-8.91,5.26-13.11,8.23-8.41,5.76-16.27,12.44-23.4,19.73-38.88,39.69-51.26,97.98-48.02,151.94.56,9.08,1.47,18.09,3.09,27l.16.81c.05.23.11.57.14.63l-33.56,4.62Z" />
                            <path class="cls-1"
                                d="M114.69,0c1.2,21.99-.84,44.11-4.81,65.71-10.02,54.13-36.84,106.43-85.4,135.17-7.79,4.72-16.06,8.69-24.48,12.09,4.48-2.61,8.91-5.26,13.11-8.23,8.41-5.76,16.27-12.44,23.4-19.73,38.88-39.69,51.26-97.98,48.02-151.94-.56-9.08-1.47-18.09-3.09-27l-.16-.81c-.05-.23-.11-.57-.14-.63L114.69,0Z" />
                        </g>
                    </g>
                </svg>
                <svg class="w-[10vw] h-[4vw] hidden md:block" viewBox="0 0 203 83" fill="none"
                    xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M20.7455 63.7981C20.7455 66.1739 20.4569 68.2768 19.8856 70.1183C19.3144 71.9597 18.3957 73.6211 17.1354 75.1024C15.8692 76.5837 14.2025 77.9662 12.1295 79.2442C10.0565 80.5222 7.4829 81.7479 4.4146 82.9387L1.0754 77.153V76.1712C4.50294 74.3298 6.92343 72.4941 8.34274 70.6527C9.75616 68.8112 10.4629 66.4412 10.4629 63.5308V57.0306L10.0094 27.4801L0.987061 27.7473L0.262695 26.9457L0.804496 19.5566H21.1989L20.6571 55.9617L20.7455 63.7923V63.7981Z"
                        fill="#7C154D" />
                    <path
                        d="M49.532 33.9803C53.8606 33.9803 57.2469 34.9272 59.6851 36.8267C62.1232 38.7263 63.3423 41.4565 63.3423 45.0174L62.8888 54.8056C62.7651 57.1815 62.665 59.1391 62.5708 60.6785C62.4824 62.2237 62.4353 63.3216 62.4353 63.9722C62.4353 65.7498 63.0949 66.6444 64.42 66.6444C65.0796 66.6444 65.8629 66.4643 66.7639 66.1099L67.665 66.8244L66.5814 72.6102C64.9559 73.6791 62.9123 74.3587 60.4448 74.655C56.8347 74.3006 54.6674 72.221 53.9489 68.4219H53.4071C50.5214 71.5065 47.4825 73.6152 44.2906 74.7421C40.3212 74.684 37.1881 73.6152 34.9031 71.5356C32.6181 69.4617 31.4756 66.6386 31.4756 63.0776C31.4756 57.6172 34.3613 54.3525 40.1387 53.2836L53.3129 50.7916L53.4012 47.0506C53.4012 43.2515 51.5049 41.352 47.7181 41.352C44.1669 41.352 40.0798 42.9843 35.4449 46.2489L34.7205 45.7145L33.366 38.6798C38.6605 35.5371 44.0432 33.9629 49.5202 33.9629L49.532 33.9803ZM41.0456 61.9333C41.0456 63.4785 41.4637 64.6925 42.3118 65.5813C43.154 66.4701 44.3259 66.9174 45.8335 66.9174C48.1775 66.9174 50.6156 65.5813 53.1421 62.9092L53.3247 56.1417L44.1198 58.0993C42.0762 58.5176 41.0515 59.7897 41.0515 61.9275L41.0456 61.9333Z"
                        fill="#7C154D" />
                    <path
                        d="M100.244 73.9461L100.969 49.467C100.969 45.0173 99.0429 42.7924 95.1914 42.7924C92.6649 42.7924 89.897 44.0995 86.8876 46.7077L86.705 56.676L87.1585 73.9461H76.3281L76.9583 57.6577L76.5048 15.3739L87.2409 14.5723L86.8817 40.4746H87.4235C89.1667 38.8713 90.9099 37.5527 92.659 36.5129C94.4022 35.4731 96.2397 34.7179 98.1655 34.2416C102.376 34.2416 105.592 35.2233 107.824 37.1809C110.05 39.1386 111.104 41.9269 110.98 45.5459L110.798 56.6702L111.157 73.9403H100.238L100.244 73.9461Z"
                        fill="#7C154D" />
                    <path
                        d="M137.512 33.9803C141.846 33.9803 145.226 34.9272 147.665 36.8267C150.103 38.7263 151.322 41.4565 151.322 45.0174L150.868 54.8056C150.745 57.1815 150.645 59.1391 150.55 60.6785C150.462 62.2237 150.415 63.3216 150.415 63.9722C150.415 65.7498 151.074 66.6444 152.4 66.6444C153.059 66.6444 153.842 66.4643 154.743 66.1099L155.644 66.8244L154.561 72.6102C152.935 73.6791 150.892 74.3587 148.424 74.655C144.814 74.3006 142.647 72.221 141.928 68.4219H141.387C138.501 71.5065 135.462 73.6152 132.27 74.7421C128.301 74.684 125.174 73.6152 122.883 71.5356C120.598 69.4617 119.455 66.6386 119.455 63.0776C119.455 57.6172 122.341 54.3525 128.118 53.2836L141.292 50.7916L141.381 47.0506C141.381 43.2515 139.484 41.352 135.698 41.352C132.146 41.352 128.053 42.9843 123.424 46.2489L122.706 45.7145L121.351 38.6798C126.646 35.5371 132.029 33.9629 137.506 33.9629L137.512 33.9803ZM129.031 61.9333C129.031 63.4785 129.449 64.6925 130.291 65.5813C131.133 66.4701 132.305 66.9174 133.813 66.9174C136.157 66.9174 138.595 65.5813 141.122 62.9092L141.304 56.1417L132.099 58.0993C130.056 58.5176 129.031 59.7897 129.031 61.9275V61.9333Z"
                        fill="#7C154D" />
                    <path
                        d="M187.87 73.9468L188.412 49.4677C188.412 45.018 186.486 42.7931 182.635 42.7931C180.049 42.7931 177.252 44.1001 174.243 46.7084V56.6766L174.784 73.9468H163.954L164.496 57.7455L164.042 35.404L174.331 34.5153V40.4811H174.873C178.183 37.2745 181.793 35.2007 185.703 34.248C189.914 34.248 193.135 35.2298 195.361 37.1874C197.588 39.145 198.642 41.9334 198.518 45.5524L198.247 56.6766L198.701 73.9468H187.87Z"
                        fill="#7C154D" />
                    <path
                        d="M100.139 20.1835L100.268 14.2118L100.139 0.345703H111.452L111.617 0.572254L111.387 2.46599L106.658 2.36724L102.653 2.40209L102.589 8.98951L106.358 9.02436L109.732 8.98951L109.897 9.15216L109.697 11.0459L102.553 11.011L102.518 14.0143L102.583 18.1561L106.487 18.191L111.446 18.0632L111.611 18.2897L111.411 20.1835H100.133H100.139Z"
                        fill="#939598" />
                    <path
                        d="M127.659 20.1835L126.799 18.586L122.135 11.8011L117.306 18.7196L116.51 20.1893H113.866L120.645 10.1397L114.096 0.351562H117.141L117.971 1.88514L122.335 8.24601L126.669 1.88514L127.5 0.351562H130.209L123.795 9.84348L130.709 20.1835H127.665H127.659Z"
                        fill="#939598" />
                    <path
                        d="M135.262 20.1832L135.391 14.2115L135.262 0.345402L141.381 0.310547C143.389 0.310547 144.92 0.804313 145.98 1.79765C147.04 2.78519 147.57 4.22582 147.57 6.11956C147.57 8.3386 146.905 10.0755 145.568 11.3244C144.237 12.5734 142.399 13.2007 140.061 13.2007H137.647L137.747 20.1832H135.268H135.262ZM144.985 6.31706C144.985 3.70882 143.607 2.34951 140.851 2.23914L137.776 2.30304L137.712 11.1792L140.986 11.2431C142.288 11.0282 143.277 10.4995 143.966 9.66305C144.649 8.82655 144.991 7.71122 144.991 6.31706H144.985Z"
                        fill="#939598" />
                    <path
                        d="M168.171 9.87242C168.171 13.2416 167.382 15.8441 165.804 17.6681C164.225 19.4921 161.993 20.41 159.108 20.41C156.222 20.41 154.243 19.5502 152.788 17.8308C151.334 16.1113 150.604 13.6425 150.604 10.4243C150.604 7.20608 151.381 4.5746 152.936 2.79123C154.49 1.00787 156.711 0.113281 159.602 0.113281C162.494 0.113281 164.473 0.949778 165.951 2.62277C167.429 4.29577 168.165 6.71232 168.165 9.86661L168.171 9.87242ZM153.124 10.1338C153.124 12.9628 153.631 15.0541 154.644 16.4134C155.656 17.7727 157.199 18.4523 159.272 18.4523C163.483 18.4523 165.592 15.7337 165.592 10.2965C165.592 7.51396 165.079 5.46338 164.055 4.14473C163.03 2.8319 161.481 2.16967 159.408 2.16967C155.221 2.16967 153.124 4.82439 153.124 10.128V10.1338Z"
                        fill="#939598" />
                    <path
                        d="M173 20.1832L173.13 14.2115L173 0.345402L179.119 0.310547C181.127 0.310547 182.658 0.786886 183.718 1.74537C184.778 2.70386 185.309 4.11545 185.309 5.98595C185.309 7.38011 184.949 8.6 184.237 9.65724C183.518 10.7145 182.488 11.5336 181.145 12.1203C181.94 13.4041 182.77 14.6646 183.642 15.9019C184.513 17.1392 185.42 18.3824 186.369 19.6197V19.916C186.039 20.0263 185.68 20.1367 185.291 20.2413C184.902 20.3516 184.49 20.4271 184.048 20.4678L183.718 20.2703C182.794 18.8994 181.946 17.5923 181.174 16.3376C180.403 15.0887 179.684 13.8862 179.025 12.7302H175.385L175.485 20.1657H173.006L173 20.1832ZM179.184 10.8539C181.545 10.1568 182.723 8.59419 182.723 6.15441C182.723 3.71463 181.345 2.34951 178.589 2.23914L175.515 2.30304L175.45 10.7551L179.19 10.8539H179.184Z"
                        fill="#939598" />
                    <path
                        d="M194.696 20.1834L194.861 14.2118L194.732 2.30329H192.682L189.107 2.43109L188.942 2.16968L189.143 0.339844H202.8L203 0.566395L202.8 2.42528L199.296 2.29748H197.246L197.117 14.0084L197.217 20.1718H194.702L194.696 20.1834Z"
                        fill="#939598" />
                </svg>
                <div
                    :class="{ 'cursor-pointer md:block hidden group select-none': true, 'cairo': currentLanguage === 'en', 'montserrat': currentLanguage === 'ar', 'vazir' : currentLanguage==='ir' }">
                    <div class="text-[1.2vw] hidden md:block">{{ t('lang') }}</div>
                    <div
                        class="absolute cursor-default group-hover:opacity-100 translate-y-2 group-hover:translate-y-0 opacity-0 transition-all duration-200 bg-white drop-shadow-lg px-[0.6vw] w-[10vw] h-[8.4vw] rounded-[0.2vw] mt-[2vw]">
                        <div class="h-1/3 w-full flex items-center justify-between">
                            <div class="cairo text-[0.8vw]">عربي</div>
                            <div :class="{ 'w-[3.4vw] cursor-pointer h-[1.6vw]  border-[#D9C6CB] border-2 rounded-full transition-all duration-200': true, 'bg-[#F1DEE3]': currentLanguage !== 'ar', 'bg-[#791A4D]': currentLanguage === 'ar' }"
                                @click="changeLang('ar')">
                                <img src="@/public/assets/images/arabic.svg"
                                    :class="{ 'w-[1.5vw] h-[1.2vw] transition-all duration-200': true, 'translate-x-[1.6vw] rtl:translate-x-[-1.6vw]': currentLanguage === 'ar', 'translate-x-0 rtl:translate-x-0': currentLanguage != 'ar' }">
                            </div>
                        </div>
                        <div class="w-full h-[0.5px] bg-[#D9C6CB]"></div>
                        <div class="h-1/3 w-full  items-center justify-between md:flex hidden">
                            <div class="montserrat text-[0.8vw]">English</div>
                            <div :class="{ 'w-[3.4vw] cursor-pointer h-[1.6vw]  border-[#D9C6CB] border-2 rounded-full transition-all duration-200': true, 'bg-[#F1DEE3]': currentLanguage !== 'en', 'bg-[#791A4D]': currentLanguage === 'en' }"
                                @click="changeLang('en')">
                                <img src="@/public/assets/images/eng.svg"
                                    :class="{ 'w-[1.5vw] h-[1.2vw] transition-all duration-200': true, 'translate-x-[1.6vw] rtl:translate-x-[-1.6vw]': currentLanguage === 'en', 'translate-x-0 rtl:translate-x-0': currentLanguage !== 'en' }">
                            </div>

                        </div>
                        <div class="w-full h-[0.5px] bg-[#D9C6CB]"></div>
                        <div class="h-1/3 w-full  items-center justify-between md:flex hidden">
                            <div class="vazir text-[0.8vw]">فارسی</div>
                            <div :class="{ 'w-[3.4vw] cursor-pointer h-[1.6vw]  border-[#D9C6CB] border-2 rounded-full transition-all duration-200': true, 'bg-[#F1DEE3]': currentLanguage !== 'ir', 'bg-[#791A4D]': currentLanguage === 'ir' }"
                                @click="changeLang('ir')">
                                <img src="@/public/assets/images/128px-Flag_of_Iran.svg.png"
                                    :class="{ 'w-[1.2vw] rounded-full h-[1.2vw] transition-all duration-200': true, 'translate-x-[1.6vw] rtl:translate-x-[-1.6vw]': currentLanguage === 'ir', 'translate-x-0 rtl:translate-x-0': currentLanguage !== 'ir' }">
                            </div>

                        </div>
                    </div>
                </div>
            </NuxtLink>
          
            <div class="md:flex hidden rtl:flex-row-reverse justify-between items-center space-x-[3.9vw]">
                <NuxtLink class="select-none cursor-pointer text-[1.2vw]" to="/">
                    {{ t('home') }}
                </NuxtLink>
                <div>
                    <div @mouseenter="closeHovers" 
                        class="select-none cursor-pointer rtl:flex-row-reverse group flex items-center space-x-[0.4vw] text-[1.2vw]">
                        <div  @click.self="goToProducts" class="cursor-pointer">{{ t('products') }}</div>
                        <svg class="group-hover:rotate-180 rotate-0 transition-all duration-200" width="0.7vw"
                            height="0.35vw" viewBox="0 0 18 10" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M17 1.52539L9.83673 8.81216C9.44952 9.20605 8.8163 9.21142 8.42247 8.82415L1 1.52539"
                                stroke="#1F2120" stroke-width="1.3" stroke-linecap="round" />
                        </svg>
                        <div class="absolute origin-top z-0 group-hover:z-30 w-[10vw] transition-all duration-200 translate-y-[12vw] group-hover:translate-y-[10vw]  group-hover:opacity-100 opacity-0 h-[16vw] ">
                            <div v-if="productList.length>0"
                            class="w-[10vw] rounded-[0.2vw] bg-white drop-shadow-md">
                            <div  class="w-full group cursor-pointer flex items-center px-[0.4vw] py-[0.6vw] justify-between h-[2vw] bg-white transition-all duration-200 text-[0.8vw] hover:bg-[#FFE6ED]"
                                v-for="(item, index) in productList" :key="index"
                                
                                @click="onElementHover(index, item.subcategories && item.subcategories.length > 0)">
                                <div @click.self="goToCategory(item.slug,'Products',item.title,'منتجات',item.title_arabic)"> {{ currentLanguage === 'en' ? item.title : (currentLanguage==='ir' ? item.title_persian : item.title_arabic) }}</div>
                                <div>
                                    <svg v-if="item.subcategories && item.subcategories.length > 0"
                                        :class="{ 'rotate-0': currentLanguage === 'ar' || currentLanguage==='ir', 'rotate-180': currentLanguage === 'en' }"
                                        width="1.2vw" height="1.2vw" viewBox="0 0 24 24" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <g id="icon">
                                            <path id="icon_2" d="M14 17L9 12L14 7V17Z" fill="#1F2120" />
                                        </g>
                                    </svg>

                                </div>
                                <div :class="{ 'absolute w-[10vw] transition-all duration-200 z-20  rounded-[0.2vw] rtl:translate-x-[-9.7vw] rtl:pr-[0.3vw] ltr:pl-[0.3vw] ltr:translate-x-[9.7vw]': true, 'opacity-0 ': !hoverState[index], 'opacity-100': hoverState[index] }"
                                    v-if="item.subcategories && item.subcategories.length > 0 && hoverState[index]">
                                 <div class="bg-white">
                                    <div class="px-[0.4vw] py-[0.6vw] h-[2vw] hover:bg-[#FFE6ED] bg-white transition-all duration-200 " @click="goToCategory(category.slug,item.title,category.title,item.title_arabic,category.title_arabic)"
                                        v-for="(category, index) in item.subcategories" :key="index">
                                        {{ currentLanguage === 'en' ? category.title : (currentLanguage==='ir' ? category.title_persian: category.title_arabic) }}
                                    </div>
                                 </div>
                                </div>
                            </div>
                        </div>
                        </div>
                    
                    </div>

                </div>
                <NuxtLink class="select-none cursor-pointer text-[1.2vw]" to="/contactUs">
                    {{ t('contactUs') }}
                </NuxtLink>
            </div>
        </div>
        <div class="w-full px-[3.75vw]">
            <div class="block md:hidden h-[1px] bg-black w-full"></div>
        </div>
        <!-- Drawer -->
        <div 
         @click.self="toggleDrawer" :class="['w-[100vw] z-30 overflow-hidden h-[100vh]  ltr:justify-start rtl:justify-items-end bg-black/50 fixed top-0 backdrop-blur-sm duration-200 transition-opacity', drawerPositioned ? 'opacity-100 ' : ' opacity-0 ',drawerOpened ? 'flex' : ' hidden']">
            <div class="relative" @click.self="toggleDrawer">
                <div :class="{'relative transition-all duration-200 p-3 rtl:rounded-l-2xl ltr:rounded-r-2xl max-h-[100vh] bg-white w-[90vw] max-w-[360px]':true,'rtl:translate-x-[70vw] ltr:translate-x-[-70vw]': !drawerPositioned,'translate-x-0': drawerPositioned}">
                    <div
                        class="flex rtl:left-0 ltr:right-0 justify-between items-center">
                        <div class="flex items-center ">
                            <svg id="Layer_2" class=" w-24 h-24" data-name="Layer 2" xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 223.19 215.27">
                                <defs>

                                </defs>
                                <g id="Layer_1-2" data-name="Layer 1">
                                    <g>
                                        <path class="cls-2"
                                            d="M111.6,189.36c-45.07,0-81.73-36.66-81.73-81.73S66.53,25.91,111.6,25.91s81.73,36.66,81.73,81.73-36.66,81.73-81.73,81.73ZM111.6,53.01c-30.12,0-54.63,24.51-54.63,54.63s24.51,54.63,54.63,54.63,54.63-24.51,54.63-54.63-24.51-54.63-54.63-54.63Z" />
                                        <path class="cls-1"
                                            d="M108.5,215.27c-1.2-21.99.84-44.11,4.81-65.71,10.02-54.13,36.84-106.43,85.4-135.17,7.79-4.72,16.06-8.69,24.48-12.09-4.48,2.61-8.91,5.26-13.11,8.23-8.41,5.76-16.27,12.44-23.4,19.73-38.88,39.69-51.26,97.98-48.02,151.94.56,9.08,1.47,18.09,3.09,27l.16.81c.05.23.11.57.14.63l-33.56,4.62Z" />
                                        <path class="cls-1"
                                            d="M114.69,0c1.2,21.99-.84,44.11-4.81,65.71-10.02,54.13-36.84,106.43-85.4,135.17-7.79,4.72-16.06,8.69-24.48,12.09,4.48-2.61,8.91-5.26,13.11-8.23,8.41-5.76,16.27-12.44,23.4-19.73,38.88-39.69,51.26-97.98,48.02-151.94-.56-9.08-1.47-18.09-3.09-27l-.16-.81c-.05-.23-.11-.57-.14-.63L114.69,0Z" />
                                    </g>
                                </g>
                            </svg>
                            <svg class=" w-40 h-16" viewBox="0 0 203 83" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M20.7455 63.7981C20.7455 66.1739 20.4569 68.2768 19.8856 70.1183C19.3144 71.9597 18.3957 73.6211 17.1354 75.1024C15.8692 76.5837 14.2025 77.9662 12.1295 79.2442C10.0565 80.5222 7.4829 81.7479 4.4146 82.9387L1.0754 77.153V76.1712C4.50294 74.3298 6.92343 72.4941 8.34274 70.6527C9.75616 68.8112 10.4629 66.4412 10.4629 63.5308V57.0306L10.0094 27.4801L0.987061 27.7473L0.262695 26.9457L0.804496 19.5566H21.1989L20.6571 55.9617L20.7455 63.7923V63.7981Z"
                                    fill="#7C154D" />
                                <path
                                    d="M49.532 33.9803C53.8606 33.9803 57.2469 34.9272 59.6851 36.8267C62.1232 38.7263 63.3423 41.4565 63.3423 45.0174L62.8888 54.8056C62.7651 57.1815 62.665 59.1391 62.5708 60.6785C62.4824 62.2237 62.4353 63.3216 62.4353 63.9722C62.4353 65.7498 63.0949 66.6444 64.42 66.6444C65.0796 66.6444 65.8629 66.4643 66.7639 66.1099L67.665 66.8244L66.5814 72.6102C64.9559 73.6791 62.9123 74.3587 60.4448 74.655C56.8347 74.3006 54.6674 72.221 53.9489 68.4219H53.4071C50.5214 71.5065 47.4825 73.6152 44.2906 74.7421C40.3212 74.684 37.1881 73.6152 34.9031 71.5356C32.6181 69.4617 31.4756 66.6386 31.4756 63.0776C31.4756 57.6172 34.3613 54.3525 40.1387 53.2836L53.3129 50.7916L53.4012 47.0506C53.4012 43.2515 51.5049 41.352 47.7181 41.352C44.1669 41.352 40.0798 42.9843 35.4449 46.2489L34.7205 45.7145L33.366 38.6798C38.6605 35.5371 44.0432 33.9629 49.5202 33.9629L49.532 33.9803ZM41.0456 61.9333C41.0456 63.4785 41.4637 64.6925 42.3118 65.5813C43.154 66.4701 44.3259 66.9174 45.8335 66.9174C48.1775 66.9174 50.6156 65.5813 53.1421 62.9092L53.3247 56.1417L44.1198 58.0993C42.0762 58.5176 41.0515 59.7897 41.0515 61.9275L41.0456 61.9333Z"
                                    fill="#7C154D" />
                                <path
                                    d="M100.244 73.9461L100.969 49.467C100.969 45.0173 99.0429 42.7924 95.1914 42.7924C92.6649 42.7924 89.897 44.0995 86.8876 46.7077L86.705 56.676L87.1585 73.9461H76.3281L76.9583 57.6577L76.5048 15.3739L87.2409 14.5723L86.8817 40.4746H87.4235C89.1667 38.8713 90.9099 37.5527 92.659 36.5129C94.4022 35.4731 96.2397 34.7179 98.1655 34.2416C102.376 34.2416 105.592 35.2233 107.824 37.1809C110.05 39.1386 111.104 41.9269 110.98 45.5459L110.798 56.6702L111.157 73.9403H100.238L100.244 73.9461Z"
                                    fill="#7C154D" />
                                <path
                                    d="M137.512 33.9803C141.846 33.9803 145.226 34.9272 147.665 36.8267C150.103 38.7263 151.322 41.4565 151.322 45.0174L150.868 54.8056C150.745 57.1815 150.645 59.1391 150.55 60.6785C150.462 62.2237 150.415 63.3216 150.415 63.9722C150.415 65.7498 151.074 66.6444 152.4 66.6444C153.059 66.6444 153.842 66.4643 154.743 66.1099L155.644 66.8244L154.561 72.6102C152.935 73.6791 150.892 74.3587 148.424 74.655C144.814 74.3006 142.647 72.221 141.928 68.4219H141.387C138.501 71.5065 135.462 73.6152 132.27 74.7421C128.301 74.684 125.174 73.6152 122.883 71.5356C120.598 69.4617 119.455 66.6386 119.455 63.0776C119.455 57.6172 122.341 54.3525 128.118 53.2836L141.292 50.7916L141.381 47.0506C141.381 43.2515 139.484 41.352 135.698 41.352C132.146 41.352 128.053 42.9843 123.424 46.2489L122.706 45.7145L121.351 38.6798C126.646 35.5371 132.029 33.9629 137.506 33.9629L137.512 33.9803ZM129.031 61.9333C129.031 63.4785 129.449 64.6925 130.291 65.5813C131.133 66.4701 132.305 66.9174 133.813 66.9174C136.157 66.9174 138.595 65.5813 141.122 62.9092L141.304 56.1417L132.099 58.0993C130.056 58.5176 129.031 59.7897 129.031 61.9275V61.9333Z"
                                    fill="#7C154D" />
                                <path
                                    d="M187.87 73.9468L188.412 49.4677C188.412 45.018 186.486 42.7931 182.635 42.7931C180.049 42.7931 177.252 44.1001 174.243 46.7084V56.6766L174.784 73.9468H163.954L164.496 57.7455L164.042 35.404L174.331 34.5153V40.4811H174.873C178.183 37.2745 181.793 35.2007 185.703 34.248C189.914 34.248 193.135 35.2298 195.361 37.1874C197.588 39.145 198.642 41.9334 198.518 45.5524L198.247 56.6766L198.701 73.9468H187.87Z"
                                    fill="#7C154D" />
                                <path
                                    d="M100.139 20.1835L100.268 14.2118L100.139 0.345703H111.452L111.617 0.572254L111.387 2.46599L106.658 2.36724L102.653 2.40209L102.589 8.98951L106.358 9.02436L109.732 8.98951L109.897 9.15216L109.697 11.0459L102.553 11.011L102.518 14.0143L102.583 18.1561L106.487 18.191L111.446 18.0632L111.611 18.2897L111.411 20.1835H100.133H100.139Z"
                                    fill="#939598" />
                                <path
                                    d="M127.659 20.1835L126.799 18.586L122.135 11.8011L117.306 18.7196L116.51 20.1893H113.866L120.645 10.1397L114.096 0.351562H117.141L117.971 1.88514L122.335 8.24601L126.669 1.88514L127.5 0.351562H130.209L123.795 9.84348L130.709 20.1835H127.665H127.659Z"
                                    fill="#939598" />
                                <path
                                    d="M135.262 20.1832L135.391 14.2115L135.262 0.345402L141.381 0.310547C143.389 0.310547 144.92 0.804313 145.98 1.79765C147.04 2.78519 147.57 4.22582 147.57 6.11956C147.57 8.3386 146.905 10.0755 145.568 11.3244C144.237 12.5734 142.399 13.2007 140.061 13.2007H137.647L137.747 20.1832H135.268H135.262ZM144.985 6.31706C144.985 3.70882 143.607 2.34951 140.851 2.23914L137.776 2.30304L137.712 11.1792L140.986 11.2431C142.288 11.0282 143.277 10.4995 143.966 9.66305C144.649 8.82655 144.991 7.71122 144.991 6.31706H144.985Z"
                                    fill="#939598" />
                                <path
                                    d="M168.171 9.87242C168.171 13.2416 167.382 15.8441 165.804 17.6681C164.225 19.4921 161.993 20.41 159.108 20.41C156.222 20.41 154.243 19.5502 152.788 17.8308C151.334 16.1113 150.604 13.6425 150.604 10.4243C150.604 7.20608 151.381 4.5746 152.936 2.79123C154.49 1.00787 156.711 0.113281 159.602 0.113281C162.494 0.113281 164.473 0.949778 165.951 2.62277C167.429 4.29577 168.165 6.71232 168.165 9.86661L168.171 9.87242ZM153.124 10.1338C153.124 12.9628 153.631 15.0541 154.644 16.4134C155.656 17.7727 157.199 18.4523 159.272 18.4523C163.483 18.4523 165.592 15.7337 165.592 10.2965C165.592 7.51396 165.079 5.46338 164.055 4.14473C163.03 2.8319 161.481 2.16967 159.408 2.16967C155.221 2.16967 153.124 4.82439 153.124 10.128V10.1338Z"
                                    fill="#939598" />
                                <path
                                    d="M173 20.1832L173.13 14.2115L173 0.345402L179.119 0.310547C181.127 0.310547 182.658 0.786886 183.718 1.74537C184.778 2.70386 185.309 4.11545 185.309 5.98595C185.309 7.38011 184.949 8.6 184.237 9.65724C183.518 10.7145 182.488 11.5336 181.145 12.1203C181.94 13.4041 182.77 14.6646 183.642 15.9019C184.513 17.1392 185.42 18.3824 186.369 19.6197V19.916C186.039 20.0263 185.68 20.1367 185.291 20.2413C184.902 20.3516 184.49 20.4271 184.048 20.4678L183.718 20.2703C182.794 18.8994 181.946 17.5923 181.174 16.3376C180.403 15.0887 179.684 13.8862 179.025 12.7302H175.385L175.485 20.1657H173.006L173 20.1832ZM179.184 10.8539C181.545 10.1568 182.723 8.59419 182.723 6.15441C182.723 3.71463 181.345 2.34951 178.589 2.23914L175.515 2.30304L175.45 10.7551L179.19 10.8539H179.184Z"
                                    fill="#939598" />
                                <path
                                    d="M194.696 20.1834L194.861 14.2118L194.732 2.30329H192.682L189.107 2.43109L188.942 2.16968L189.143 0.339844H202.8L203 0.566395L202.8 2.42528L199.296 2.29748H197.246L197.117 14.0084L197.217 20.1718H194.702L194.696 20.1834Z"
                                    fill="#939598" />
                            </svg>
                        </div>
                        <svg @click="toggleDrawer" class=" cursor-pointer" width="24" height="25" viewBox="0 0 24 25" fill="none"
                            xmlns="http://www.w3.org/2000/svg">
                            <g id="Icon">
                                <path id="icon"
                                    d="M6.4 19.3623L5 17.9623L10.6 12.3623L5 6.7623L6.4 5.3623L12 10.9623L17.6 5.3623L19 6.7623L13.4 12.3623L19 17.9623L17.6 19.3623L12 13.7623L6.4 19.3623Z"
                                    fill="#1F2120" />
                            </g>
                        </svg>

                    </div>
                    <div class="w-full h-[1px] bg-[#D9C6CB] "></div>
                    <NuxtLink to="/"  @click="toggleDrawer"
                        :class="{ 'w-full h-10 text-[22px] my-1 cursor-pointer p-4 bg-white transition-all duration-200 hover:bg-[#FFE6ED] flex items-center': true, 'montserrat': currentLanguage === 'en', 'cairo': currentLanguage === 'ar', 'vazir' : currentLanguage==='ir' }">
                        <div>{{ t('home') }}</div>
                    </NuxtLink>
                  
                    <div @click.self="openProfucts"
                        :class="{ 'w-full h-10 text-[22px] my-1 cursor-pointer p-4 bg-white transition-all duration-200 flex justify-between items-center': true, 'montserrat': currentLanguage === 'en', 'cairo': currentLanguage === 'ar','vazir' : currentLanguage==='ir', 'bg-[#FFE6ED]': productsOpen }">
                        <div @click.self="goToProducts"> {{ t('products') }}</div>
                        <div>
                            <svg :class="{ '-rotate-90': !productsOpen, 'rotate-90': productsOpen, 'transition-all duration-200': true }"
                                width="24" height="24" viewBox="0 0 24 24" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <g id="icon">
                                    <path id="icon_2" d="M14 17L9 12L14 7V17Z" fill="#1F2120" />
                                </g>
                            </svg>
                        </div>
                    </div>
                    <div v-if="productsOpen" class="w-full max-h-[90vw] overflow-y-scroll flex py-2 px-3 space-x-2 justify-between">
                        <!-- <div class=" bg-black w-[1px] mx-2 rounded-full"></div> -->
                        <div class="w-full">
                            <div v-for="(item, index) in productList" @click="openProductGroup(index,item.subcategories && item.subcategories.length >0)" :key="index">
                                <div
                                    :class="{ 'w-full px-3 cursor-pointer transition-all duration-200 flex justify-between items-center h-10 lrt:text-left': true,'bg-[#FFE6ED]' : drawerState[index], 'bg-white' : !drawerState[index] ,'hover:bg-[#FFE6ED]': !item.childCategories || item.childCategories.length === 0, 'montserrat': currentLanguage === 'en', 'cairo': currentLanguage === 'ar' }" >
                                    <div @click.self="goToCategory(item.slug,'Products',item.title,'منتجات',item.title_arabic)">
                                        {{ currentLanguage ==='en' ? item.title : (currentLanguage==='ir'?  item.title_persian  : item.title_arabic) }}
                                    </div>
                                    <div>
                                        <svg :class="{ '-rotate-90': !drawerState[index], 'rotate-90': drawerState[index], 'transition-all duration-200': true }"
                                            width="24" height="24" viewBox="0 0 24 24" fill="none"
                                            xmlns="http://www.w3.org/2000/svg"
                                            v-if="item.subcategories && item.subcategories.length > 0">
                                            <g id="icon">
                                                <path id="icon_2" d="M14 17L9 12L14 7V17Z" fill="#1F2120" />
                                            </g>
                                        </svg>
                                    </div>
                                </div>
                                <div class=" py-1 flex space-x-2 justify-between" v-if="drawerState[index]">
                                    <div class=" bg-black w-[1px] mx-2 rounded-full"></div>
                                    <div class="w-full">
                                        <div class="bg-white w-full h-10 py-4 transition-all duration-200 flex items-center cursor-pointer px-3 hover:bg-[#FFE6ED]" v-for="(category,index) in item.subcategories" :key="index">
                                         <div @click.self="goToCategory(category.slug,'Products',category.title,'منتجات',category.title_arabic)" :class="currentLanguage==='en' ? 'montserrat' : (currentLanguage==='ir' ? 'vazir' : 'cairo')">
                                            {{ currentLanguage === 'en' ? category.title : (currentLanguage==='ir' ? category.title_persian : category.title_arabic) }}
                                         </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                           
                        </div>
                      
                    </div>
                    <NuxtLink  @click.self="toggleDrawer" to="/contactUs"
                        :class="{ 'w-full h-10 text-[22px] my-1 cursor-pointer p-4 bg-white transition-all duration-200 hover:bg-[#FFE6ED] flex items-center': true, 'montserrat': currentLanguage === 'en', 'cairo': currentLanguage === 'ar', 'vazir' : currentLanguage==='ir' }">
                        <div>{{ t('contactUs') }}</div>
                    </NuxtLink>
                    <div class="px-6">
                                <div class="h-[1px] my-2 bg-[#D9C6CB] w-full"></div>
                            </div>
                    <div @click="toggleLang" :class="{'cursor-pointer transition-all duration-200 flex justify-between px-3 py-2 items-center' : true, 'bg-[#FFE6ED]': languageOpened,'bg-white': !languageOpened}">
                        <div :class="{ 'montserrat' : currentLanguage==='en', 'cairo' : currentLanguage ==='ar', 'vazir' : currentLanguage==='ir','text-[22px]':true }">{{ t('language') }}</div>
                        <svg :class="{ '-rotate-90': !languageOpened, 'rotate-90': languageOpened, 'transition-all duration-200': true }"
                                            width="24" height="24" viewBox="0 0 24 24" fill="none"
                                            xmlns="http://www.w3.org/2000/svg"
                                            >
                                            <g id="icon">
                                                <path id="icon_2" d="M14 17L9 12L14 7V17Z" fill="#1F2120" />
                                            </g>
                                        </svg>
                    </div>
                    <div v-if="languageOpened">
                        <div class="w-full flex items-center justify-between px-3 my-3">
                            <div class="cairo text-[16px]">عربي</div>
                            <div :class="{ 'w-[54px] cursor-pointer h-[28px]  border-[#D9C6CB] border-2 rounded-full transition-all duration-200': true, 'bg-[#F1DEE3]': currentLanguage !== 'ar', 'bg-[#791A4D]': currentLanguage === 'ar' }"
                                @click="changeLang('ar')">
                                <img src="@/public/assets/images/arabic.svg"
                                    :class="{ 'w-[32px] h-[24px] transition-all duration-200': true, 'translate-x-[21px] rtl:translate-x-[-21px]': currentLanguage === 'ar', 'translate-x-0 rtl:translate-x-0': currentLanguage != 'ar' }">
                            </div>
                        </div>
                        <div class="w-full items-center justify-between flex px-3 my-3">
                            <div  class="montserrat text-[16px]">English</div>
                            <div :class="{ 'w-[54px] cursor-pointer h-[28px]  border-[#D9C6CB] border-2 rounded-full transition-all duration-200': true, 'bg-[#F1DEE3]': currentLanguage !== 'en', 'bg-[#791A4D]': currentLanguage === 'en' }"
                                @click="changeLang('en')">
                                <img src="@/public/assets/images/eng.svg"
                                    :class="{ 'w-[32px] h-[24px] transition-all duration-200': true, 'translate-x-[21px] rtl:translate-x-[-21px]': currentLanguage === 'en', 'translate-x-0 rtl:translate-x-0': currentLanguage !== 'en' }">
                            </div>

                        </div>
                        <div class="w-full items-center justify-between flex px-3 my-3">
                            <div style="font-family: 'Vazir'" class="vazir text-[16px]">فارسی</div>
                            <div :class="{ 'w-[54px] cursor-pointer h-[28px]  border-[#D9C6CB] border-2 rounded-full transition-all duration-200': true, 'bg-[#F1DEE3]': currentLanguage !== 'ir', 'bg-[#791A4D]': currentLanguage === 'ir' }"
                                @click="changeLang('ir')">
                                <img src="@/public/assets/images/128px-Flag_of_Iran.svg.png"
                                    :class="{ 'w-[24px] h-[24px] rounded-full transition-all duration-200': true, 'translate-x-[21px] rtl:translate-x-[-21px]': currentLanguage === 'ir', 'translate-x-0 rtl:translate-x-0': currentLanguage !== 'ir' }">
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { useI18n } from 'vue-i18n';
import { categoryStore } from '~/store/category-state.js';
import { loadingStore } from '~/store/loading-state';
export default {
    computed:{
        currentRoute() {
      return this.$route.path;
    },
    currentRouteTitle(){
      if(!this.$route.path.includes('productDetail')){
        switch(this.currentRoute){
           case "/products" : 
            return this.t('products')
           case "/contactUs" : 
            return this.t('contactUs');
           case "/" : 
             return this.t('home')
       }
      }else{
        return this.t('productDetail')
      }
    },
    isProductDetailPage() {
      // Checks if the current route path starts with '/productDetail'
      return this.$route.path.startsWith('/productDetail');
    }
    },
    setup() {
        const { t, locale } = useI18n();
        onMounted(() => {
            const savedLanguage = localStorage.getItem('appLanguage');
            if (savedLanguage) {
                locale.value = savedLanguage;
            }

        });
        function changeLang(lang) {
          if(currentLanguage.value === 'ir' && lang === currentLanguage.value){
          locale.value = 'en';
          }else{
            if (currentLanguage.value === 'en' && lang === currentLanguage.value) {
                locale.value = 'ar';
            } else if (currentLanguage.value === 'ar' && lang === currentLanguage.value) {
                locale.value = 'en';
            } else if (currentLanguage.value !== lang) {
                locale.value = lang;
            }
          }
            localStorage.setItem('appLanguage', locale.value);
            window.location.reload();
        }

        const currentLanguage = computed(() => locale.value);

        return {
            t,
            changeLang,
            currentLanguage,
        };
    },
    props: {
        productList: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            categoryState : categoryStore(),
            loadingState:loadingStore(),
            hoverState: [],
            drawerState:[],
            productsOpen: false,
            drawerOpened:false,
            languageOpened:false,
            drawerPositioned:false,
            drawerAnimationTime:200,
        }
    },
    watch: {
        productList(newValue, oldValue) {
            for (let a = 0; a < this.productList.length; a++) {
                this.hoverState.push(false);
                this.drawerState.push(false);
            }
        },
    },
    methods: {
        closeHovers(){
            for(let a=0;a< this.hoverState.length;a++){
                this.hoverState[a] = false;
            }
        },
        goToProducts(){
            this.$router.push('/products');
            this.toggleDrawer()
        },
        goToProducts(){
            this.categoryState.setFirstCategory('Products')
            this.categoryState.setSecondCategory('')
            this.categoryState.setFirstCategoryArabic('منتجات')
            this.categoryState.setSecondCategoryArabic('')
            this.categoryState.setFilter('')
            if(this.drawerOpened){
                this.drawerPositioned = false;
                setTimeout(()=>{
                    this.drawerOpened = false
                    for(let a=0; a< this.drawerState.length;a++){
                        this.drawerState[a]= false;
                    }
                },this.drawerAnimationTime);
            }
            if(this.currentRoute!=='/products'){
                this.$router.push('/products');
            }else{
                
            }
        },
        goToCategory(filter,firstCategory,secondCategory,arabicFirstCategory,arabicSecondCategory){
            this.categoryState.setFirstCategory(firstCategory)
            this.categoryState.setSecondCategory(secondCategory)
            this.categoryState.setFirstCategoryArabic(arabicFirstCategory)
            this.categoryState.setSecondCategoryArabic(arabicSecondCategory)
            this.categoryState.setFilter(filter)
            if(this.drawerOpened){
                this.drawerPositioned = false;
                setTimeout(()=>{
                    this.drawerOpened = false
                    for(let a=0; a< this.drawerState.length;a++){
                        this.drawerState[a]= false;
                    }
                },this.drawerAnimationTime);
            }
            if(this.currentRoute!=='/products'){
                this.$router.push('/products');
            }else{
                
            }
        },
        fetchCategories(){
              
        },
        onElementHover(index, hasChilderen) {
            for(let a=0;a< this.hoverState.length;a++){
                this.hoverState[a] = false;
            }
            if (hasChilderen) {
                this.hoverState[index] = true;
            }
        },
        openProfucts() {
            this.productsOpen = !this.productsOpen;
            if(this.productsOpen){
                this.languageOpened = false;
            }
        },
        toggleDrawer(){
            if(this.drawerOpened){
                this.drawerPositioned = false;
                setTimeout(()=>{
                    this.drawerOpened = false
                    for(let a=0; a< this.drawerState.length;a++){
                        this.drawerState[a]= false;
                    }
                },this.drawerAnimationTime);
            }else{
                this.drawerOpened = true;
                
                setTimeout(()=>{this.drawerPositioned = true;},10)
            }
        },
        onElementMouseLeave(index, hasChilderen) {
            if (hasChilderen) {
                this.hoverState[index] = false;
            }
        },
        openProductGroup(index,hasChilderen){
            for(let a=0;a<this.hoverState.length;a++){
                this.hoverState[a] = false;
            }
if(hasChilderen){
    this.drawerState[index] = !this.drawerState[index];
}
        },
        toggleLang(){
            this.languageOpened = !this.languageOpened;
            if(this.languageOpened){
                for(let a=0;a<this.hoverState.length;a++){
                this.hoverState[a] = false;
            }
            this.productsOpen = false;
            }
        }
    },
};
</script>

<style>
.cls-1 {
    fill: #7c154d;
}

.cls-1,
.cls-2 {
    stroke-width: 0px;
}

.cls-2 {
    fill: #a8aaad;
}
</style>