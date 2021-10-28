<template>
    <div>
        <h1>Team View</h1>
        <TeamList />
    </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import TeamList from '@/components/TeamList.vue'

@Options({
    components: {
        TeamList,
    }
})
export default class Teams extends Vue {}
</script>