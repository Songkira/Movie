<template>
  <div id="test" style="display: column; justify-content: center;">
    <div id="watchinput">
      <h1 style="margin-top: 30px; padding-top:20px;color:pink;">보고싶은 영화</h1>
      <div style="display: flex; justify-content: center;">
        <input style="width:80%;" class="form-control" type="text" v-model.trim="watchList" placeholder="보고싶은 영화는?">
        <br>
        <button @click="createWatch" class="btn btn-light">Add</button>
      </div>
    </div>
    <WatchListItem v-for="(watch, index) in getWatchList" :key="index" :watch="watch" :index="index"
    />
  </div>
</template>


<script>
import WatchListItem from '@/views/WatchListItem.vue'

export default {
  name: 'WatchListView',
  components: {
    WatchListItem
  },
  data() {
    return {
      watchList: null,
    }
  },
  computed: {
    getWatchList() {
      console.log(this.$store.state.watchesList)
      return this.$store.state.watchesList
    }
  },
  methods: {
    createWatch() {
      this.$store.dispatch('createWatch', this.watchList)
      this.watchList = null
    }
  }
}
</script>

<style>
.test {
  height: 100%;
}
#watchinput {
  display: flex column;
  text-align: center;
  width: 80%;
  height: 200px;
  margin: auto;
  background-color: rgb(31, 7, 43);
  border-radius: 5px;
}
#test {
  height: 100vh;
}
</style>