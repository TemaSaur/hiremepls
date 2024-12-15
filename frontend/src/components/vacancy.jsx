import Inner from "./vacancy_inner"

export default function({vacancy}) {
    return <a className="vacancy bg-soft py-2 p-4" href={`/vacancies/${vacancy.slug}`}>
        <Inner vacancy={vacancy}/>
    </a>
}