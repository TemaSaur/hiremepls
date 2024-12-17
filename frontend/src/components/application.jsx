import VacancyInner from "./vacancy_inner"

export default function Application({application}) {
    const statusColor = {
        'ожидание': 'wait',
        'принято': 'accepted',
        'отказ': 'rejected',
    }[application.status]

    const status = <span className={statusColor}>{application.status}</span>

    return <div className="application bg-soft py-2 p-4">
        <VacancyInner vacancy={application.vacancy} status={status}></VacancyInner>
    </div>
}