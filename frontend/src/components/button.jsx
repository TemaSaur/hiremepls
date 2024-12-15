export default function Button({active=True, children}) {
    const color = active ? 'bg-[#AAAEFF]' : 'bg-[#E5E5EB]'
    return <button className={`cursor rounded-lg py-1 px-4 ${color}`}>
        {children}
    </button>
}