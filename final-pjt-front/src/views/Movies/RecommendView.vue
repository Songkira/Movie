<template>
  <div>
    <div style="width:10%">

    </div>
    <div style="width:90%">
      <RecommandListViewVue/>
    </div>
  </div>
</template>

<script>
import RecommandListViewVue from '@/views/Movies/RecommandListView';

export default {
  name: 'RecommendView',
  components: { RecommandListViewVue },

}
</script>

<style>

</style>