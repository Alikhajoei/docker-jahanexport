import { defineStore } from 'pinia';

export const categoryStore = defineStore('categoryStore', {
    state: () => ({
        firstCategory:'Category1',
        secondCategory:'Category2',
        firstCategoryArabic:'دسته بندی اول',
        secondCategoryArabic:'دسته بندی دوم',
        firstCategoryPersian:'',
        secondCategoryPersian:'',
        filter:'',
      }),
      actions: {
        setFirstCategory(newFirstCategory) {
          this.firstCategory = newFirstCategory
        },
        setSecondCategory(newSecondCategory){
          this.secondCategory = newSecondCategory
        },
        setFirstCategoryArabic(newFirstCategoryArabic){
          this.firstCategoryArabic = newFirstCategoryArabic
        },
        setSecondCategoryArabic(newSecondCategoryArabic){
          this.secondCategoryArabic = newSecondCategoryArabic
        },
        setFirstCategoryPersian(newFirstCategoryPersian){
        this.firstCategoryPersian = newFirstCategoryPersian
        },
        setSecondCategoryPersian(newSecondCategoryPersian){
            this.secondCategoryPersian = newSecondCategoryPersian
        },
        setFilter(newFilter){
          this.filter = newFilter
        }
    }
});