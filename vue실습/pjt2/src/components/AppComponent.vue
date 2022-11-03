<template>
  <div>
    <h2>App</h2>
		<input type="text" v-model="appData">
		<p>parentData: {{ parentData }} </p>
		<p>childData: {{childData }}</p>
		<AppParentComponent 
		:appData="appData"
		@parent-input-change="fromParentInputChange"
		@gogo="gogoChild"
		/>
  </div>
</template>


<script>
import AppParentComponent from './AppParentComponent.vue'

export default {
	name: 'AppComponent',
	components : {
		AppParentComponent
	},

	data() {
		return {
			appData: '',
			parentData:'',
			childData:'',
		}
	},
	methods: {
		fromParentInputChange(parentInputData) {
			this.parentData=parentInputData

		},
		gogoChild(ChildInputData) {
			this.childData=ChildInputData
		}
	}

}
</script>

<style>

</style>