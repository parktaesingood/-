<template>
  <div>
    <input type="text"
    v-model.trim="todoTitle"
    @keyup.enter="createTodo"
    >
  </div>
</template>

<script>
export default {
    name:'TodoForm',
    data() {
        return {
            todoTitle: null,
        }
    },
    methods: {
        createTodo() {
            console.log(this.todoTitle)
            // this.$ 전역
            if (this.todoTitle) {
                this.$store.dispatch('createTodo', this.todoTitle)
            
            }
            this.todoTitle = null
        }
    }
}
</script>

<style>

</style>