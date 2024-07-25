const { dbClient } = require('../utils/db');

class QueryController {
    // Searches by Month
    static async getPaintings(req, res) {
        try {
            const { months, colors, subjects, title , episode, fields, limit, page, sortBy } = req.query;

            // convert month abbreviation to numeric format
            const monthAbbreviationToNumber = (month) => {
                const monthMap = {
                    jan: '01', feb: '02', mar: '03', apr: '04', may: '05', jun: '06',
                    jul: '07', aug: '08', sep: '09', oct: '10', nov: '11', dec: '12'
                };
                return monthMap[month.toLowerCase()];
            };


            const filter = {};
            if (months) {
                const monthList = months.split(',').map(month => {
                    if (isNaN(month)) {
                        return monthAbbreviationToNumber(month);
                    }
                    return month.padStart(2, '0');
                });
                const monthRegexes = monthList.map(monthNumber => `^${monthNumber}`);
                filter.air_date = { $regex: new RegExp(monthRegexes.join('|')) };
            }

            if (colors) {
                const colorList = colors.split(',').map(color => color.trim());
                filter['colors.name'] = { $in: colorList };
            }

            if (title) {
                filter.title= { $regex: title, $options: 'i' };
            }
            if (episode) {
                filter.episode = episode
            }

            if (subjects) {
                const subjectList = subjects.split(',');
                filter.subjects = { $in: subjectList };
            }

            // fields to display using projection objection
            const projection = {
                _id: 0,
                title: 1,
                air_date: 1,
                episode: 1,
                img_src: 1,
                youtube_src: 1
            };

            // sorting and pagination options 


            const pageNumber = parseInt(page) || 1
            const pageSize = parseInt(limit) || 10
            const skip = (pageNumber - 1) * pageSize

            const sortOption = sortBy ? { id: sortBy } : { id: 1 };

            const paintings = await dbClient.findPaintings(filter, projection, skip, pageSize, sortOption);

            if (!paintings) {
                res.status(400).json('No paintings found with given parameters');
            }
            res.setHeader('Content-Type', 'application/json');
            res.status(200).send(JSON.stringify(paintings, null, 2) + '\n');
        } catch (err) {
            console.error('Error fetching paintings: ', err);
            res.status(500).send('Internal Server Error')
        }
    }
}

module.exports = QueryController;
