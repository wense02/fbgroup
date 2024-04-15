import React, { useState } from 'react';
import axios from 'axios';

const SearchGroups = () => {
    const [townName, setTownName] = useState('');
    const [radius, setRadius] = useState('');
    const [groups, setGroups] = useState([]);

    const handleSearch = async () => {
        try {
            const response = await axios.get(`/search-groups/?town_name=${townName}&radius=${radius}`);
            setGroups(response.data.groups);
        } catch (error) {
            console.error('Error fetching groups:', error);
        }
    };

    return (
        <div>
            <h2>Search Groups</h2>
            <div>
                <label>Town Name:</label>
                <input type="text" value={townName} onChange={(e) => setTownName(e.target.value)} />
            </div>
            <div>
                <label>Radius:</label>
                <input type="text" value={radius} onChange={(e) => setRadius(e.target.value)} />
            </div>
            <button onClick={handleSearch}>Search</button>
            <div>
                <h3>Groups:</h3>
                <ul>
                    {groups.map((group, index) => (
                        <li key={index}>
                            <strong>{group.name}</strong>
                            <p>Description: {group.description}</p>
                            <p>Member Count: {group.member_count}</p>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default SearchGroups;
