<template>
  <div>
    <div v-for="(comment, idx) in comments" :key="idx" >
      <span class="left margin-left">{{ comment.user.username }} : {{ comment.content }}</span>
      <span class="right margin-right">
        {{ $moment(comment.created_at).format('YY-MM-DD HH:mm') }}
        <div v-if="username === comment.user.username">
          <b-button variant="outline-danger" @click="deleteComment(comment.id)">X</b-button>
        </div>        
      </span>
    </div>
    <br><br>
  </div>
</template>

<script>
export default {
  props: {
    // 왼쪽 부모에서의 이름
    comments: Array,
    username: String,
  },
  methods: {
    deleteComment: function (comment_id) {
      this.$emit('deleteComment', comment_id)
    }
  }
}
</script>

<style>
.left {
  display: flex;
  justify-content: flex-start;
}

.margin-left{
  margin-left: 100px;
}

.right {
  display: flex;
  justify-content: flex-end;
}

.margin-right{
  margin-right: 100px
}

</style>