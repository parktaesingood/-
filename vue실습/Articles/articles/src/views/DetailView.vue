<template>
 <!-- 매개변수가 있다면 함수 ( ) 안에 값을 넣어준다 -->
  <div>
    <h1>Detail</h1>
    <!-- optional chaniing 객체가 있을 때만 출력 -->
    <p>글 번호 : {{ article?.id }}</p>
    <p>글 제목 : {{ article?.title }}</p>
    <p>글 내용 : {{ article?.content }}</p>
    <p>글 작성시간 : {{ articleCreatedAt }}</p>
    <router-link :to="{ name: 'index'}">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
    name: 'DetailView',
    data() {
        return {
            article: null,
        }
    },
    computed: { 
        articles() {
            return this.$store.state.articles
        },
        articleCreatedAt() {
            const article = this.article
            const createdAt = new Date(article?.createdAt).toLocaleString()
            return createdAt
        }
    },
    methods: {
        getArticleById(id) {
            // const id = this.$route.params.id
            for (const article of this.articles) {
                if (article.id === Number(id)) {
                    this.article = article
                    break
                }
            }
        },
        created() {
        this.getArticleById(this.$route.params.id)
    }
    }

}
</script>

<style>

</style>