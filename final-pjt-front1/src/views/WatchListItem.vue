<template>
  <div class="card" style="margin: auto; width: 80%; justify-content: center;"> 
    <ul class="list-group list-group-flush"  @click="updateWatch" :class="{'is_selected' : watch.selected }">
      <li class="list-group-item" v-if="index % 2" style="background-color:white">{{ watch.title }}</li>
      <li class="list-group-item" v-if="index % 2== 0" style="background-color:lightgray">{{ watch.title }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
    watch: Object, 
    index: Number,
  },
  methods: {
    updateWatch () {
      this.$store.dispatch('updateWatch', this.watch )
    }
  },
}
</script>

<style>
div {
  margin: auto;
}
.is_selected {
  text-decoration: line-through;
  color: lightgray;
}
</style>