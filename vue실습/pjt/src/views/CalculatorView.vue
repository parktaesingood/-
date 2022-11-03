<template>
<div>
    <h1>소득세 계산기</h1>
    <div>
        <label for="income">연봉 입력 (만원):</label>
        <input type="number" id="income" v-model.number="income">
    </div>

    <div>
        <label for="tax-credit">세액 감면액(만원):</label>
        <input type="number" id="tax-credit" v-model.number="taxCredit">
    </div>

		<hr>

		<TotalIncome :income="income" :tax-credit="taxCredit"/>
  </div>
</template>

<script>
import TotalIncome from '../components/TotalIncome.vue'

export default {
    name: 'CalculatorView',
		components: {
			TotalIncome
		},
    data() {
        return {
            income: 0,
            taxCredit: 0,
        }
    }

}
</script>

<style>

</style>