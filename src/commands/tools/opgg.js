const { SlashCommandBuilder } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
    .setName('opgg')
    .setDescription('Look up a League of Legends player on OP.GG')
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
        const newMessage = `https://www.op.gg/summoners/${interaction.options.get('region').value}/${interaction.options.get('name').value.replaceAll(' ', '+')}`
        await interaction.editReply({
            content: newMessage
        });
    }
}