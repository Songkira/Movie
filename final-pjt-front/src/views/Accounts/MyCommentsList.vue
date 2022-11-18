<template>
    <div class="card" style="width: 540px; height: auto;" @click="detailGo">
        <div class="row g-0">
            <div class="col">
                <img :src="image_url" class="img-fluid rounded-start" alt="..." style="height: 210px;">
            </div>
            <div class="col-md-9">
                <div class="card-body" style="height: 210px; display: flex column; justify-content:center;">
                    <h5 class="card-title">{{ movieinfo.title }}</h5>
                    <br>
                    <div>
                        <h6 class="card-title" style="margin: 5%;">{{ comment.content }}</h6>
                    </div>
                </div>
            </div>
        </div>
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

</style>