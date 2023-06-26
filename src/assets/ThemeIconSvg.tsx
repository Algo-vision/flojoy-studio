type IconProps = {
  color?: string;
};

export const DarkIcon = ({ color = "#000000" }: IconProps) => {
  return (
    <svg
      width="22"
      height="22"
      viewBox="0 0 22 22"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M9.375 18.054C6.77083 18.054 4.55729 17.1764 2.73437 15.4211C0.911458 13.6659 0 11.5345 0 9.02699C0 6.51949 0.911458 4.38812 2.73437 2.63287C4.55729 0.877624 6.77083 0 9.375 0C9.61805 0 9.85694 0.00835842 10.0917 0.0250751C10.3257 0.0417917 10.5556 0.0668665 10.7812 0.1003C10.0694 0.585083 9.50104 1.21597 9.07604 1.99296C8.65035 2.77062 8.4375 3.6108 8.4375 4.5135C8.4375 6.01799 8.98437 7.29682 10.0781 8.34997C11.1719 9.40312 12.5 9.92969 14.0625 9.92969C15.0174 9.92969 15.8941 9.72474 16.6927 9.31485C17.4913 8.90563 18.1424 8.35833 18.6458 7.67294C18.6806 7.89026 18.7066 8.11159 18.724 8.33693C18.7413 8.56294 18.75 8.79296 18.75 9.02699C18.75 11.5345 17.8385 13.6659 16.0156 15.4211C14.1927 17.1764 11.9792 18.054 9.375 18.054ZM9.375 16.048C10.9028 16.048 12.2743 15.6428 13.4896 14.8324C14.7049 14.0213 15.5903 12.9638 16.1458 11.6599C15.7986 11.7434 15.4514 11.8103 15.1042 11.8605C14.7569 11.9106 14.4097 11.9357 14.0625 11.9357C11.9271 11.9357 10.1083 11.2129 8.60625 9.76721C7.10486 8.32088 6.35417 6.56964 6.35417 4.5135C6.35417 4.17916 6.38021 3.84483 6.43229 3.5105C6.48437 3.17616 6.55382 2.84183 6.64062 2.5075C5.28646 3.04243 4.18854 3.89498 3.34687 5.06515C2.50451 6.23531 2.08333 7.55593 2.08333 9.02699C2.08333 10.9661 2.79514 12.6211 4.21875 13.9918C5.64236 15.3626 7.36111 16.048 9.375 16.048Z"
        fill={color}
      />
    </svg>
  );
};

export const LightIcon = ({ color = "#000000" }: IconProps) => {
  return (
    <svg
      width="22"
      height="22"
      viewBox="0 0 22 22"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M11 14C11.8333 14 12.5417 13.7083 13.125 13.125C13.7083 12.5417 14 11.8333 14 11C14 10.1667 13.7083 9.45833 13.125 8.875C12.5417 8.29167 11.8333 8 11 8C10.1667 8 9.45833 8.29167 8.875 8.875C8.29167 9.45833 8 10.1667 8 11C8 11.8333 8.29167 12.5417 8.875 13.125C9.45833 13.7083 10.1667 14 11 14ZM11 16C9.61667 16 8.43767 15.5123 7.463 14.537C6.48767 13.5623 6 12.3833 6 11C6 9.61667 6.48767 8.43733 7.463 7.462C8.43767 6.48733 9.61667 6 11 6C12.3833 6 13.5627 6.48733 14.538 7.462C15.5127 8.43733 16 9.61667 16 11C16 12.3833 15.5127 13.5623 14.538 14.537C13.5627 15.5123 12.3833 16 11 16ZM1 12C0.716667 12 0.479333 11.904 0.288 11.712C0.096 11.5207 0 11.2833 0 11C0 10.7167 0.096 10.479 0.288 10.287C0.479333 10.0957 0.716667 10 1 10H3C3.28333 10 3.521 10.0957 3.713 10.287C3.90433 10.479 4 10.7167 4 11C4 11.2833 3.90433 11.5207 3.713 11.712C3.521 11.904 3.28333 12 3 12H1ZM19 12C18.7167 12 18.4793 11.904 18.288 11.712C18.096 11.5207 18 11.2833 18 11C18 10.7167 18.096 10.479 18.288 10.287C18.4793 10.0957 18.7167 10 19 10H21C21.2833 10 21.5207 10.0957 21.712 10.287C21.904 10.479 22 10.7167 22 11C22 11.2833 21.904 11.5207 21.712 11.712C21.5207 11.904 21.2833 12 21 12H19ZM11 4C10.7167 4 10.4793 3.904 10.288 3.712C10.096 3.52067 10 3.28333 10 3V1C10 0.716667 10.096 0.479 10.288 0.287C10.4793 0.0956666 10.7167 0 11 0C11.2833 0 11.521 0.0956666 11.713 0.287C11.9043 0.479 12 0.716667 12 1V3C12 3.28333 11.9043 3.52067 11.713 3.712C11.521 3.904 11.2833 4 11 4ZM11 22C10.7167 22 10.4793 21.904 10.288 21.712C10.096 21.5207 10 21.2833 10 21V19C10 18.7167 10.096 18.4793 10.288 18.288C10.4793 18.096 10.7167 18 11 18C11.2833 18 11.521 18.096 11.713 18.288C11.9043 18.4793 12 18.7167 12 19V21C12 21.2833 11.9043 21.5207 11.713 21.712C11.521 21.904 11.2833 22 11 22ZM4.65 6.05L3.575 5C3.375 4.81667 3.279 4.58333 3.287 4.3C3.29567 4.01667 3.39167 3.775 3.575 3.575C3.775 3.375 4.01667 3.275 4.3 3.275C4.58333 3.275 4.81667 3.375 5 3.575L6.05 4.65C6.23333 4.85 6.325 5.08333 6.325 5.35C6.325 5.61667 6.23333 5.85 6.05 6.05C5.86667 6.25 5.63767 6.34567 5.363 6.337C5.08767 6.329 4.85 6.23333 4.65 6.05ZM17 18.425L15.95 17.35C15.7667 17.15 15.675 16.9127 15.675 16.638C15.675 16.3627 15.7667 16.1333 15.95 15.95C16.1333 15.75 16.3627 15.6543 16.638 15.663C16.9127 15.671 17.15 15.7667 17.35 15.95L18.425 17C18.625 17.1833 18.721 17.4167 18.713 17.7C18.7043 17.9833 18.6083 18.225 18.425 18.425C18.225 18.625 17.9833 18.725 17.7 18.725C17.4167 18.725 17.1833 18.625 17 18.425ZM15.95 6.05C15.75 5.86667 15.6543 5.63733 15.663 5.362C15.671 5.08733 15.7667 4.85 15.95 4.65L17 3.575C17.1833 3.375 17.4167 3.279 17.7 3.287C17.9833 3.29567 18.225 3.39167 18.425 3.575C18.625 3.775 18.725 4.01667 18.725 4.3C18.725 4.58333 18.625 4.81667 18.425 5L17.35 6.05C17.15 6.23333 16.9167 6.325 16.65 6.325C16.3833 6.325 16.15 6.23333 15.95 6.05ZM3.575 18.425C3.375 18.225 3.275 17.9833 3.275 17.7C3.275 17.4167 3.375 17.1833 3.575 17L4.65 15.95C4.85 15.7667 5.08767 15.675 5.363 15.675C5.63767 15.675 5.86667 15.7667 6.05 15.95C6.25 16.1333 6.346 16.3627 6.338 16.638C6.32933 16.9127 6.23333 17.15 6.05 17.35L5 18.425C4.81667 18.625 4.58333 18.7207 4.3 18.712C4.01667 18.704 3.775 18.6083 3.575 18.425Z"
        fill={color}
      />
    </svg>
  );
};