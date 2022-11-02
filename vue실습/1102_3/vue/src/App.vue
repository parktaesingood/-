<template>
  <div id="app">
    <TodoList :todos="todos" @delete-todo="deleteTodo"/>
    <TodoForm @create-todo="creataeTodo"/>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'


export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return{
      todos: [],
    }
  },
  methods: {
    creataeTodo: function (todoTitle) {
      const todo = {
        title: todoTitle
      }
      this.todos.push(todo)
      },
      deleteTodo: function (todo) {
        const index = this.todos.indexOf(todo)
        this.todos.splice(index, 1)
      }
  }
}
</script>

<style>

  
</style>
