<template>
  <div id="app">
    <TodoHeader></TodoHeader>
    <TodoInput v-on:addTodoItem="addOneItem"></TodoInput>
    <TodoList v-bind:propsdata="todoItems" v-on:removeItem="removeOneItem"></TodoList>
    <TodoFooter v-on:clearAll="clearAllItems"></TodoFooter>
    
  </div>
</template>

<script>
import TodoHeader from './components/TodoHeader.vue'
import TodoInput from './components/TodoInput.vue'
import TodoList from './components/TodoList.vue'
import TodoFooter from './components/TodoFooter.vue'

import axios from 'axios';



export default {
  components: {
    'TodoHeader' : TodoHeader,
    'TodoInput' : TodoInput,
    'TodoList' : TodoList,
    'TodoFooter' : TodoFooter
  },
  data () {
    return {
      todoItems: []
    }
  },

  methods: {

    getTodoItems: function() {
      axios.get('http://localhost:8080/todos')
      .then((res) => {
        this.todoItems = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    addOneItem: function(newTodoItem) {
      const todoItem = new FormData();
      todoItem.append('content', newTodoItem)
      axios.post("http://localhost:8080/todo", todoItem)
      .then((res) => {
        console.log(res.data);
        this.getTodoItems();
      })
      .catch((err) => {
        console.log(err);
      })
    // 비동기라서 여기에 함수 쓰면 요청 처리되기 전에 수행됨 => 그래서 엔터 치자마자 안 나옴
    // this.getTodoItems();
    },
    removeOneItem: function(todoItem) {
      var targetId = todoItem.todoId;
      
      axios.delete(`http://localhost:8080/todo/${targetId}`)
      .then((res) => {
        console.log(res.data);
        this.getTodoItems();
      })
      .catch((err) => {
        console.log(err);
      })
    },
    clearAllItems: function() {
      axios.delete('http://localhost:8080/todos/all')
      .then((res) => {
        console.log(res.data);
        this.getTodoItems();
      })
      .catch((err) => {
        console.log(err);
      })
    }

  },
  created: function() {
    this.getTodoItems()
  }
}
</script>

<style>
  body {
    text-align: center;
    background-color: #F6F6F6;
    /* background-color: lemonchiffon; */
  }

  input {
    border-style: groove;
    width: 200px;
  }

  button {
    border-style: groove;
  }

  .shadow {
    box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.03);
  }


</style>
