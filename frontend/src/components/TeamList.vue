<template>
    <div>
        <ul v-for="team in teams" :key="team.name">
            <TeamRow v-bind:team="team" @reload="reload()"/>
        </ul>
    </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'
import TeamRow from '@/components/TeamRow.vue'
import { api } from '@/api'
import { Team } from '@/models/team'

async function loadTeams(): Promise<Team[]> {
    const resp = await api.get('teams')
    return resp.data as Team[]
}

@Options({
    components: {
        TeamRow,
    }
})
export default class TeamList extends Vue {
    teams: Team[] = []

    public mounted(): void {
        this.reload()
    }

    public reload(): void {
        loadTeams().then(
            (teams) => this.teams = teams,
            (error) => console.log(error)
        )
    }
}
</script>