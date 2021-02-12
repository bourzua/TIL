<template>
  <div>
    <!-- ul>li*3 -->
    <ul>
      <li v-for="(todoItem, idx) in propsdata" :key="idx" class="shadow">
        <span>{{ todoItem.content }}</span>        
        <span class="removeBtn" v-on:click="removeTodo(todoItem)">
            <i class="far fa-trash-alt"></i>
        </span>    
      </li>
    </ul>
  </div>
</template>

<script>

export default {
  props: ['propsdata'],  
  methods: {
    removeTodo: function(todoItem) {
      console.log(todoItem.content);
      console.log(todoItem.todoId);
      this.$emit('removeItem', todoItem);
    },
    
  },
  
  
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
  margin-top: 0;
  text-align: left;
}

li {
  display: flex;
  min-height: 50px;
  height: 50px;
  line-height: 50px;
  margin: 0.5rem 0;
  padding: 0 0.9rem;
  background: white;
  border-radius: 5px;
}

.removeBtn {
  margin-left: auto;
  color: #de4343;
}

.checkBtn {
  line-height: 50px;
  color: #62acde;
  margin-right: 5px;
}

.checkBtnCompleted {
  color: #b3adad;
}

.textCompleted {
  text-decoration: line-through;
  color: #b3adad;
}

</style>