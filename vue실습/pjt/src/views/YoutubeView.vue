<template>
  <div class="container">
    <div>
        <h1 class="text-primary">SSAFY</h1>    
    </div>
    

    <section v-if="isSelectedVideo" class="mt-4">
        <div class="ratio ratio-16x9">
            <iframe :src="videoSrc" frameborder="0"></iframe>
        </div>
        <div class="video-title shadow p-3 mb-5 bg-body rounded ">
        {{ selectedVideo.snippet.title }}
        </div>
    </section>
    
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'

const API_URL = "https://www.googleapis.com/youtube/v3/search"
const API_KEY = 'AIzaSyB_zni6-hWaxut34-EmzwSrdW6EWgjpsb8'
export default {
    name: 'YoutubeView',
    created() {
        axios.get(API_URL, {
            params: {
                key: API_KEY,
                type: 'video',
                part: 'snippet',
                q: '코딩노래'
            }
        }).then((response) => {
            this.videos = response.data.items
            this.selectedVideo = this.videos[0]
        }).catch((error) => {
            console.log(error)
        })
    },
    data() {
        return {
            videos: [],
            selectedVideo: {}
        }
    },
    computed : {
        videoSrc() {
            const url = 'http://www.youtube.com/embed/'
            return url + this.selectedVideo.id.videoId
        },
        isSelectedVideo() {
            // 길이가 1 이상이면 True
            return !!Object.keys(this.selectedVideo).length
        }
    }
}
</script>

<style>
* {
    font-family: 'Noto Sans KR', sans-serif;
}

.video-title {
    border: 3px solid green;
}
</style>