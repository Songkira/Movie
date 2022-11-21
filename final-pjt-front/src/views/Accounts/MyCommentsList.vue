<template>
    <div style="display: flex; justify-content: center; margin:2%;" @click="detailGo">
        <span class="col-3 col-xl-2 row">
            <img :src="image_url" id="mycommentimage" alt="...">
        </span>
        <span class="col-9 col-xl-10" style="display: flex column; justify-content: center; background-color: #161e27; border-radius: 4px;">
            <div style="margin-top: 3%;">
                <h5><b>{{ movieinfo.title }}</b></h5>
                <div>
                    <p style="margin: 5%; margin-bottom: 0%;">{{ comment.content }}</p>
                </div>
            </div>
        </span>
    </div>
</template>

<script>

export default {
    name: 'MyCommentsList',
    props: {
        comment: Object
    },
    data() {
        return {
            movieinfo: {},
            image_url: '',
        }
    },
    created() {
        const movies = this.$store.state.movies
        for (let i=0; i<movies.length; i++) {
            if (movies[i].id === this.comment.movie_id) {
                this.movieinfo = movies[i]
                this.image_url = `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ movies[i].poster_path }`
                break
            }
        }
    },
    methods: {
        detailGo() {
            this.$router.push({ name:"DetailView", params: { id: this.movieinfo.id } })
        }
    }
}
</script>

<style>
#mycommentimage {
    object-fit: fill;
    border-radius: 5px;
}
</style>