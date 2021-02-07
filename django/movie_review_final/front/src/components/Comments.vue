<template>
  <div>
    <div>
  <b-input-group id="control_width">
    <b-form-input type="text" @keyup.enter="commentCreate"></b-form-input>
    <b-input-group-append>
      <b-button variant="info" style="color:white" @click="commentCreate">입력</b-button>
    </b-input-group-append>
  </b-input-group>
</div>
    <!-- <input @keyup.enter="commentCreate" type="text">
    <button @click="commentCreate">입력</button> -->
  </div>
</template>

<script>
export default {
  name: 'Comments',
  methods: {
    commentCreate: function (event) {
      this.$emit('createComment', event.target.value)
      event.target.value = ''
    }
  },

}
</script>

<style>

#control_width {
  width: 70%;
  margin: 0 auto;
}

</style>