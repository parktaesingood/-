<template>
  <div>
    <h2>산출새엑계산</h2>
    <p>산출세액: {{ afterTax }} 만원</p>
    <p>세액감면 : (-) {{ taxCredit }}</p>
    <hr>
    <p>결정세액: {{ finalTax }} </p>
  </div>
</template>

<script>
export default {
    name: 'TaxRate',
    props: {
        taxBase: Number,
        taxCredit: Number
    },
    computed: {
        afterTax() {
            if (this.taxBase <= 1200) {
                return Math.round(this.taxBase * 0.06)
            } else if (this.taxBase <= 4600) {
                return Math.round(this.taxBase * 0.15 -108)
            } else if (this.taxBase <= 8800) {
                return Math.round(this.taxBase * 0.24 -552)
            } else if (this.taxBase <= 15000) {
                return Math.round(this.taxBase * 0.35 -1490)
            } else if (this.taxBase <= 30000) {
                return Math.round(this.taxBase * 0.38 -1940)
            } else if (this.taxBase <= 50000) {
                return Math.round(this.taxBase * 0.40 -2540)
            } else if (this.taxBase <= 100000) {
                return Math.round(this.taxBase * 0.42 -3540)
            } else {
                return Math.round(this.taxBase * 0.45 -6540) 
            }
    },
    finalTax() {
        return this.afterTax -this.taxCredit >= 0 ? this.afterTax -this.taxCredit : 0

    }
}
}
</script>

<style>

</style>