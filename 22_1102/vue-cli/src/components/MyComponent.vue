<template>
<div class='border'>
    <h1>싸피 이거는 내가 만든 새로운 컴포넌트!</h1>
    <MyComponentItem
     static-props="MyComponent에서 보낸 데이터"
     v-bind:dynamic-props="dynamicProps"
     @child-to-parent="parentGetEvent"
     @child-input="getDynamicData "
     />

</div>
  
</template>

<script>
import MyComponentItem from '@/components/MyComponentItem'
export default {
    name: 'MyComponent',
    components : {
        MyComponentItem,
    },
    data: function () {
        return{
            dynamicProps: '이건 동적인 데이터!',
        }
    },
    methods: {
        parentGetEvent: function (childData) {
            console.log('자식컴포넌트에서 보낸 data 들엇다')
            console.log(childData)
        },
        getDynamicData: function (inputData) {
            console.log('사용자가 입력한 값은 ${inputData}입니다.')
            this.inputData = null
        }
    }

}
</script>

<style>
    .border {
        border: solid 1px black;
    }

</style>