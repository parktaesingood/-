<template>
  <div>
    <h2>appParent</h2>
    <input type="text" v-model="appParent" @input="onChildInputChange">
    <p>appData : {{ appData }}</p>
    <p>childData : {{ childData }} </p>
    <AppChildComponent 
    :app-parent="appParent"
    :app-data="appData"
    @child-input-change="fromChildInputChange"
    />
  </div>
</template>

<script>
import AppChildComponent from '../components/AppChildComponent.vue'
export default {
    name: 'AppParentComponent',
    components: {
        AppChildComponent
    },
    props: {
        appData: String,
    },
    data() {
        return {
            appParent: '',
            childData: '',
        }
    },
    methods: {
        fromChildInputChange(childInputData) {
            this.childData = childInputData
            this.$emit('gogo',childInputData)
        },
        onChildInputChange(event) {
            this.$emit('parent-input-change', event.target.value)
        }
    }

}
</script>

<style>

</style>