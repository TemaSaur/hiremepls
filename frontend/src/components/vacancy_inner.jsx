export default function({vacancy}) {
    return <>
        <div className="top">
            <span className="organization">{vacancy.organization.title}</span>
        </div>
        <div className="title text-lg my-2">{vacancy.title}</div>
        <div className="stats flex gap-4 text-xs text-softext">
            {vacancy.worktime != ''
            && <div className="worktime">{vacancy.worktime}</div>}

            {vacancy.pay != 0
            && <div className="pay">{vacancy.pay} ₽/мес</div>}
        </div>
    </>
}