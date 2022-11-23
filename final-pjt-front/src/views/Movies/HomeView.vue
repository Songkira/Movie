<template>
  <div>
    <!-- <h1>Welcome</h1> -->
    <div class="btn-group b" style=" margin-top: 10px; width: 100%; justify-content: space-evenly">
      <router-link :to="{ name: 'MovieView'}" class="rounter">
        <button class="button1" style="width:300px;"><span><i class="fa-solid fa-film">  Movie Go! </i></span></button>
      </router-link>
      <router-link :to="{ name: 'RecommendView'}" class="rounter">
        <button class="button2" style="width:300px;"><span><i class="fa-solid fa-object-group"> Recommend</i></span></button>
      </router-link>
      <router-link :to="{ name: 'RandomView'}" class="rounter">
        <button class="button3" style="width:300px;"><span><i class="fa-solid fa-gift"> Random</i></span></button>
      </router-link>
    </div>
    <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel" style="padding: 10px;" data-interval="0.1">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img :src="require(`@/assets/cinema/cinema_img0.jpg`)" alt="cinema_img">
        </div>
        <div class="carousel-item">
          <img :src="require(`@/assets/cinema/cinema_img3.jpg`)" alt="cinema_img">
        </div>
        <div class="carousel-item">
          <img :src="require(`@/assets/cinema/cinema_img4.jpg`)" alt="cinema_img">
        </div>
        <div class="carousel-item">
          <img :src="require(`@/assets/cinema/cinema_img.jpg`)" alt="cinema_img">
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'HomeView',

}
</script>

<style>
.carousel-item > img {
    /* display: block; */
    width: 100%;
    height: 80vh ;
    /* max-height: 95%이미지 높이 변경 */
  }
  .btn-group button {
    background-color:rgb(85, 85, 230); 
    border: 1px solid gray; 
    color: white; 
    padding: 10px 24px;
    cursor: pointer;
    float: left;
    border-radius: 4px;
    border: none;
    text-align: center;
    width: 200px;
    transition: all 0.5s;
    cursor: pointer;
    vertical-align:middle;
  }
  /* .b  */
  .btn-group:after {
    content: "";
    clear: both;
    display: table;
  }
  .btn-group button:not(:last-child) {
    border-right: none;
    }
  .btn-group button:hover {
    background-color: rgb(61, 213, 203);
    color: black; 
    }
  /* 화살표 나오게 */
  button span {
    cursor: pointer;
    display: inline-block;
    position: relative;
    transition: 0.5s;
  }
  button span:after {
    content: '\00bb';
    position: absolute;
    opacity: 0;
    top: 0;
    right: -20px;
    transition: 0.5s;
  }
  button:hover span {
    padding-right: 25px;
  }
  button:hover span:after {
    opacity: 1;
    right: 0;
  }
</style>