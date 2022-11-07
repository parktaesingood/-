<template>
  <div> 
    <span 
    @click="updateTodoStatus"
    :class="{ 'is-iscompleted': todo.iscompleted }"
    >
    {{ todo.title }}</span>
    <button @click="deleteTodo">Delete 

    </button>
    
    </div>
</template>

<script>
export default {
    name : 'TodoListItem',
    props: {
        todo: Object,
    },
    methods: {
        deleteTodo() {
            console.log('삭제 메서드 호출')
            this.$store.dispatch('deleteTodo',this.todo)
        },
        updateTodoStatus() {
            this.$store.dispatch('updateTodoStatus',this.todo)
        }
        
    }

}
</script>

<style>
.iscompleted {
    text-decoration-line: ;
}
</style>