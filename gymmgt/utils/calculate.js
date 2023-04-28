


export function calculateAge(dateString) {
    const today = new Date();
    const birthDate = new Date(dateString);
    let ageInDays = Math.floor((today - birthDate) / (1000 * 60 * 60 * 24));
    const ageInYears = Math.floor(ageInDays / 365);
    ageInDays -= ageInYears * 365;
    const ageInMonths = Math.floor(ageInDays / 30);
    ageInDays -= ageInMonths * 30;

    return `${ageInYears} years, ${ageInMonths} months, and ${ageInDays} days old`;
}