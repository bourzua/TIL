<template>
  <div>
    <div v-for="(comment, idx) in comments" :key="idx">
      <router-link :to="{name: 'CommunityDetail', params: {community_id: comment.community.id}}" style="color:#13c8cf">
          댓글이 달린 글: {{ comment.community.title }}
          <h5 style="color:#3b6566">{{ comment.content }}</h5>
      </router-link>
      <br>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    comments: Array,
  }

}
</script>

<style>

</style>