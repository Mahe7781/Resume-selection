const loadResumes = (role = '') => {
    const endpoint = role ? `/resumes/${role}` : '/resumes';
    fetch(`http://localhost:3000${endpoint}`)
        .then(response => response.json())
        .then(data => {
            const table = document.getElementById('resumeTable');
            table.innerHTML = '';
            if (data.length === 0) {
                table.innerHTML = `<tr><td colspan="5">No resumes found for this role.</td></tr>`;
            } else {
                data.forEach(item => {
                    const row = `
                        <tr>
                            <td>${item.email}</td>
                            <td>${item.phone}</td>
                            <td>${item.skills}</td>
                            <td>${item.score}</td>
                            <td>${item.job_role}</td>
                        </tr>
                    `;
                    table.innerHTML += row;
                });
            }
        })
        .catch(err => {
            console.error("Error fetching data:", err);
        });
};

document.addEventListener('DOMContentLoaded', () => {
    const jobRoleDropdown = document.getElementById('jobRole');
    jobRoleDropdown.addEventListener('change', () => {
        const selectedRole = jobRoleDropdown.value;
        loadResumes(selectedRole);
    });

    // Load all resumes on first load
    loadResumes();
});
