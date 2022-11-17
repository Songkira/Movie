<template>
  <div style="display: flex; justify-content: center;">
    <span style="width: 300px;">
        <Profile
        :person="person"/>
    </span>
    <span style="width: 100px;">

    </span>
    <span>
        <MyList/>
    </span>
  </div>
</template>

<script>
import Profile from '@/views/Profile.vue'
import MyList from '@/views/MyList.vue'
export default {
    name: 'MyPageView',
    data() {
      return {
        person: this.$route.params
      }
    },
    components: {
        Profile,
        MyList
    }
}
</script>

<style>

</style>