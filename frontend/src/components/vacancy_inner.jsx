export default function({vacancy, status=null}) {
    return <>
        <div className="top flex justify-between">
            <span className="organization">{vacancy.organization.title}</span>
            {status !== null ? status : <></>}
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