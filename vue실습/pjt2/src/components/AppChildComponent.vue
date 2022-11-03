<template>
    <div>
        <h1>appChild </h1>
        <input type="text" v-model="childData" @input="onChildInputChange">
        <p>appData : {{ appData }} </p>
        <p>appParent : {{ appParent }}</p>
        <p>childData : {{ childData }}</p>
        
    </div>
</template>


<script>
export default {
    name: 'AppChildComponent',
    props: {
        appData:String,
        appParent: String
    },
    data() {
        return {
            
            childData:''
        }
    },
    methods: {
        onChildInputChange(event) {
            console.log('onChildInputChange')
            this.$emit('child-input-change', event.target.value)
        }
    }

}
</script>

<style>

</style>