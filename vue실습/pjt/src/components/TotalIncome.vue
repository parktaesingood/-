<template>
  <div>
	<h2>종합 소득 금액</h2>
	<p>종합 소득 금액: {{ income }} 만원</p>
	<p>종합소득공제 : (-) 150만원 </p>
	<p>과세표준: {{ taxBase }} 만원</p>

	<hr>

	<TaxRate :tax-credit="taxCredit" :tax-base="taxBase"/>
</div>
</template>

<script>
import TaxRate from './TaxRate.vue'

export default {
    name: 'TotalIncome',
		components: {
			TaxRate
		},
    props: {
        income: Number,
        taxCredit: Number,
    },
    data() {
        return {

        }
    },
		computed: {
			taxBase() {
				return this.income -150 >= 0 ? this.income -150 : 0
			}
		}

}
</script>

<style>

</style>