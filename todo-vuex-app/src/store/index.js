import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: []
    
  },
  getters: {
  },
  mutations: {
    CREATED_TODO(state,todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state,todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index,1)
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      console.log(todoItem)
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
  },
  actions: {
    createTodo(context , todoTitle) {
      // todo 객체 만들기
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      // console.log(todoItem)
      context.commit('CREATED_TODO',todoItem)
    },
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO',todoItem)
    },
    updateTodoStatus(context,todoItem) {
      context.commit('UPDATE_TODO_STATUS',todoItem)
    }
  },
  modules: {
  }
})
