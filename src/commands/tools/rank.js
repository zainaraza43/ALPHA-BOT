const { SlashCommandBuilder, Message } = require('discord.js');
const { Client: riotClient } = require('shieldbow');

const shieldBow = new riotClient(process.env.RIOT_TOKEN);

module.exports = {
    data: new SlashCommandBuilder()
    .setName('rank')
    .setDescription('Look up the rank of a League of Legends player')
    .addStringOption(option =>
        option.setName('region')
        .setDescription('The region of the player you want to search for')
        .setRequired(true)
        .addChoices(
            { name: 'NA', value: 'na' },
            { name: 'EUW', value: 'euw' },
            { name: 'KR', value: 'kr' },
            { name: 'EUNE', value: 'eune' },
            { name: 'OCE', value: 'oce' },
            { name: 'JP', value: 'jp' },
            { name: 'BR', value: 'br' },
            { name: 'LAS', value: 'las' }, 
            { name: 'LAN', value: 'lan' },
            { name: 'RU', value: 'ru' },
            { name: 'TR', value: 'tr' },
        )
    )
    .addStringOption(option =>
        option.setName('name')
        .setDescription('The summoner name of the player')
        .setRequired(true)
    ),
    async execute(interaction, client) {
        const message = await interaction.deferReply({
            fetchReply: true
        });
        shieldBow.initialize({
            region: interaction.options.get('region').value
        })
        .then(async () => {
            const summoner = await shieldBow.summoners.fetchBySummonerName(interaction.options.get('name').value);
            const leagueEntry = await summoner.fetchLeagueEntries();
            const soloQ = leagueEntry.get('RANKED_SOLO_5x5');
            newMessage = '';
            if (soloQ.tier == 'MASTER' || soloQ.tier == 'GRANDMASTER' || soloQ.tier == 'CHALLENGER') {
                newMessage = `${summoner.name} is ${soloQ.tier} (${soloQ.lp} LP).`
            }
            else {
                newMessage = `${summoner.name} is ${soloQ.tier} ${soloQ.division} (${soloQ.lp} LP).`
            }
            await interaction.editReply({
                content: newMessage
            });
        })
        .catch(async error => {
            newMessage = `Couldn't find a summoner by the name of \"${interaction.options.get('name').value}\" in ${interaction.options.get('region').value.toUpperCase()} that has a rank.`;
            await interaction.editReply({
                content: newMessage
            });
        });
    }
}