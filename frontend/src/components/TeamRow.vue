<template>
    <li>
        <b>{{ team.name }}</b> - <small>{{ team.city }}</small> - {{ team.wins }} / {{ team.losses }}
        <button @click="addScore(true)">Add Win</button>
        <button @click="addScore(false)">Add Loss</button>
    </li>
</template>

<script lang="ts">
import { PropType } from 'vue'
import { Options, Vue } from 'vue-class-component'
import { Team } from '@/models/team'
import { api } from '@/util'

@Options({
    props: {
        team: { type: Object as PropType<Team> }
    },
    emits: ['reload']
})
export default class TeamRow extends Vue {
    team!: Team

    public addScore(win: boolean): void {
        api.post('team/' + this.team.name, null, { params: {win} }).then(
            () => this.$emit('reload')
        )
    }
}
</script>