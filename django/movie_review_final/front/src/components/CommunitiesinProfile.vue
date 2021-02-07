<template>
  <div>
    <div v-for="(community, idx) in communities" :key="idx">
      <span>
        <router-link :to="{name: 'CommunityDetail', params: {community_id: community.id}}" style="color:#13c8cf">
          {{ community.title }}
          </router-link>
        </span>
      <br>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    communities: Array,
  },
}
</script>

<style>

</style>