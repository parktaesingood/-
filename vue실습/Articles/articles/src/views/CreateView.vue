<template>
  <div>
    <h1> 게시글 작성</h1>
    <form @submit.prevent="createArticle">
        <!-- 밑의 data쪽과 양방향 연결 -->
        <input type="text" v-model="title"><br> 
        <textarea v-model="content"></textarea>
        <input type="submit">
    </form>
    <router-link :to="{ name: 'index'}">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
    name: 'CreateView',
    data() {
        return {
            title: null,
            content: null,
        }
    },
    methods: {
        createArticle() {
            const title = this.title
            const content = this.content
            const payload = {
                title, content
            }
            this.$store.dispatch('createArticle',payload)
            this.$router.push({ name: 'index' }) // 생성되자마자 index 페이지로 이동
        },
        // 그래서 id 를 넣고 params에 id
        
    },


    }

</script>

<style>

</style>